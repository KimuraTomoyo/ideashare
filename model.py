import sqlite3
# 本番（データベースから取得）
"""
# アカウントの取得
def get_user_from_db(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, role FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        keys = ["username", "password", "role"]
        return dict(zip(keys, row))
    return None

def get_ideas_from_db():
# アイデアの取得
    conn = sqlite3.connect('ideas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, title, status, likes FROM ideas")
    rows = cursor.fetchall()
    conn.close()
    keys = ["id","department","name", "category", "title", "status", "likes"]
    return [dict(zip(keys, row)) for row in rows]
def get_tags_from_db():
# タグの取得
    conn = sqlite3.connect('ideas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT tag FROM ideas")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
def get_categories1_from_db():
# カテゴリー1の取得(2と3は同じ)
    conn = sqlite3.connect('ideas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category1 FROM ideas")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
"""

# テスト用
def get_user_from_db(username):
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
    return TEST_USERS.get(username)
def get_ideas_from_db():
    return [
        {"id": 1,"department": "技術部",  "name": "田中", "category": "Tech", "title": "AI活用法", "status": "公開中", "likes": 5},
        {"id": 2,"department": "技術部",  "name": "佐藤", "category": "Health", "title": "健康アプリ", "status": "下書き", "likes": 2},
    ]

def get_tags_from_db():
    return ["AI", "健康", "教育", "環境"]

def get_categories1_from_db():
    return ["Tech", "Health", "Business"]

def get_categories2_from_db():
    return ["Web", "App", "IoT"]

def get_categories3_from_db():
    return ["企画", "研究", "開発"]


