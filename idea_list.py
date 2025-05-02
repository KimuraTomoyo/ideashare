from flask import Blueprint, render_template, request, session
from model import get_ideas_from_db
import math

# Blueprintの作成（ルーティング管理用）
idea_list_bp = Blueprint('idea_list_bp', __name__)


# アイデア一覧ページ
@idea_list_bp.route('/')
def idea_list():
    page = int(request.args.get('page', 1))
    per_page = 10
    all_ideas = get_ideas_from_db()
    total = len(all_ideas)
    total_pages = math.ceil(total / per_page)
    ideas = all_ideas[(page - 1) * per_page: page * per_page]

    return render_template('index.html', ideas=ideas, total_pages=total_pages)

# アイデア詳細ページ（省略可）
@idea_list_bp.route('/idea/<int:idea_id>')
def view_idea(idea_id):
    return f"アイデアID: {idea_id}"

# 投稿ページ（省略可）
@idea_list_bp.route('/submit')
def submit_idea():
    return "投稿ページへ"

"""
# ログアウト処理（オプション）
@idea_list_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
"""


