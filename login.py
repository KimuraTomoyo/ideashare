from flask import Flask, request, render_template, redirect, url_for, session
from idea_list import idea_list_bp  # Blueprintをインポート
from model import get_user_from_db  # ← model.pyからユーザー取得関数をインポート

# Flaskアプリの初期化
app = Flask(
    __name__,
    static_folder="static",      # CSSのフォルダ
    template_folder="templates"          # HTMLテンプレートのフォルダ
)
app.secret_key = 'some_secret_key'  # セッション使用のためのキー

# Blueprintを登録（/ideas 以下のルートを管理）
app.register_blueprint(idea_list_bp, url_prefix='/ideas')

# ログインページ表示
@app.route('/')
def index():
    return render_template('login.html')

# ログイン処理
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = get_user_from_db(username)  # ← model.pyの関数で取得
    if user and user['password'] == password:
        session['username'] = username  # セッションにユーザー名を保存
        return redirect(url_for('idea_list_bp.idea_list'))  # /ideas/ にリダイレクト
    else:
        return "ログイン失敗：ユーザー名またはパスワードが正しくありません"

# アプリ起動
if __name__ == '__main__':
    app.run(debug=True)
