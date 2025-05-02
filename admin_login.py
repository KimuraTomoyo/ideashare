from flask import Blueprint, render_template, request, redirect, url_for, session
from model import get_admin_from_db

# Blueprint の作成
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

# 管理者用ページ表示
@admin_bp.route('/admin_page', methods=['GET'])
def admin_page():
    if 'admin_username' in session:
        return render_template('admin_page.html')
    else:
        return redirect(url_for('admin_bp.admin_login_page')) 

# 管理者ログイン処理
@admin_bp.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']

    admin = get_admin_from_db(username)
    if admin and admin['password'] == password:
        session['admin_username'] = username
        return redirect(url_for('admin_bp.admin_page')) # 管理者専用ページ
    else:
        return "管理者ログイン失敗：ユーザー名またはパスワードが正しくありません"
