import sqlite3
# 本番（データベースから取得）
"""
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
    conn = sqlite3.connect('ideas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, title, status, likes FROM ideas")
    rows = cursor.fetchall()
    conn.close()
    keys = ["id","department","name", "category", "title", "status", "likes"]
    return [dict(zip(keys, row)) for row in rows]
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


