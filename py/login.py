from flask import Flask, request, render_template
# import mysql.connector  # ⭐ 後でAzure接続を使うときに有効にしてください

app = Flask(
    __name__,
    static_folder="../style",      # CSSファイルの場所
    template_folder="../"          # HTMLファイルの場所
)

# 🔁 モード切替：True = データベースモード（Azure）、False = テストユーザーモード
USE_DATABASE = False

# 🧪 テスト用ユーザー（DBを使わない時）
TEST_USERS = {
    'admin': {
        'password': 'admin123',
        'role': 'admin'
    },
    'user': {
        'password': 'user123',
        'role': 'user'
    }
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/style/<path:filename>')
def style(filename):
    return app.send_static_file(filename)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if USE_DATABASE:
        # ⭐ まだMySQLを設定していない場合、この部分はコメントのままにしてください
        """
        try:
            # ✅ ここをAzureのMySQL接続情報に変更してください
            conn = mysql.connector.connect(
                host='your-azure-mysql-host.mysql.database.azure.com',
                user='yourusername@your-azure-mysql-host',
                password='yourpassword',
                database='yourdatabasename'
            )
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                if user['role'] == 'admin':
                    return render_template('admin_home.html', username=username)
                else:
                    return render_template('user_home.html', username=username)
            else:
                return "ログイン失敗：ユーザー名またはパスワードが正しくありません"

        except mysql.connector.Error as err:
            return f"データベース接続エラー: {err}"
        """
        return "⚠ データベースモードが有効ですが、接続設定がコメントアウトされています。"
    else:
        # 🧪 テストモードでのユーザー認証
        user = TEST_USERS.get(username)
        if user and user['password'] == password:
            if user['role'] == 'admin':
                return render_template('admin_home.html', username=username)
            else:
                return render_template('user_home.html', username=username)
        else:
            return "ログイン失敗：ユーザー名またはパスワードが正しくありません"

if __name__ == '__main__':
    app.run(debug=True)
