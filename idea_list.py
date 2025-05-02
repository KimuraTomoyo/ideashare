from flask import Blueprint, render_template, request, session
import math

# Blueprintの作成（ルーティング管理用）
idea_list_bp = Blueprint('idea_list_bp', __name__)

# テスト用のダミーデータ
ideas_data = [
    {"id": 1, "name": "田中", "category": "Tech", "title": "AI活用法", "status": "公開中", "likes": 5},
    {"id": 2, "name": "佐藤", "category": "Health", "title": "健康アプリ", "status": "下書き", "likes": 2},
    # 必要に応じてさらにデータを追加可能
]

# アイデア一覧ページ
@idea_list_bp.route('/')
def idea_list():
    page = int(request.args.get('page', 1))
    per_page = 10
    total = len(ideas_data)
    total_pages = math.ceil(total / per_page)
    ideas = ideas_data[(page - 1) * per_page: page * per_page]

    username = session.get('username')  # ログインユーザー（表示には使用しない）

    return render_template('index.html', ideas=ideas, total_pages=total_pages)

# 「いいね」ボタンの処理
@idea_list_bp.route('/like/<int:idea_id>', methods=['POST'])
def like_idea(idea_id):
    for idea in ideas_data:
        if idea["id"] == idea_id:
            idea["likes"] += 1
            break
    return '', 204

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


