from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
from idea_list import idea_list_bp  # Blueprintをインポート
import os

# Flaskアプリの初期化
app = Flask(
    __name__,
    static_folder="static",          # CSSのフォルダ
    template_folder="templates"     # HTMLテンプレートのフォルダ
)
app.secret_key = 'some_secret_key'  # ※本番環境では環境変数で管理推奨

# Blueprintを登録（/ideas 以下のルートを管理）
app.register_blueprint(idea_list_bp, url_prefix='/ideas')

# データベースモード切り替え
USE_DATABASE = False

# テスト用ユーザー情報
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

# ログインページ表示
@app.route('/')
def index():
    return render_template('login.html')

# CSSファイルの配信（例: /style/style.css でアクセス）
@app.route('/style/<path:filename>')
def style(filename):
    return send_from_directory(os.path.abspath("../style"), filename)

# ログイン処理
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if USE_DATABASE:
        return "データベースモードが有効ですが、接続設定が未実装です。"
    else:
        user = TEST_USERS.get(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('idea_list_bp.idea_list'))  # 正確な関数名を確認すること
        else:
            return "ログイン失敗：ユーザー名またはパスワードが正しくありません"

# アプリ起動
if __name__ == '__main__':
    app.run(debug=True)
