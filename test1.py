import pymysql
import function_db 
# DB 연결 정보 설정

if __name__ == "__main__":
    conn = pymysql.connect(
        host="172.30.1.92",
        user="testuser",
        password="Test12./",
        database="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        # conn을 각 함수에 전달
        users = function_db.fetch_users(conn)
        for user in users:
            print(user)
        print("=== insert ===")
        function_db.insert_user(conn, "Alice", 25)
        function_db.insert_user(conn, "Bob", 30)
        users = function_db.fetch_users(conn)
        for user in users:
            print(user)        
        print("=== update ===")
        function_db.update_user(conn, 1, 25)
        users = function_db.fetch_users(conn)
        for user in users:
            print(user)
        print("=== delete ===")
        function_db.delete_user(conn, 1)
        users = function_db.fetch_users(conn)
        for user in users:
            print(user)

    finally:
        conn.close()