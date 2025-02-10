def create_table(conn):
    with conn.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS test_tab (
            name VARCHAR(20),
             id VARCHAR(20)
        );
        """
        cursor.execute(sql)
    conn.commit()

def insert_user(conn, name, id):
    name = str(name)
    id = str(id)
    with conn.cursor() as cursor:
        sql = "INSERT INTO test_tab(name, id) VALUES(%s, %s);"
        cursor.execute(sql, (name, id))
    conn.commit()

def fetch_users(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM test_tab;")
        users = cursor.fetchall()
        return users

def update_user(conn, new_id, user_id):
    new_id = str(new_id)
    user_id = str(user_id)
    with conn.cursor() as cursor:
        sql = "UPDATE test_tab SET id = %s WHERE id = %s;"
        cursor.execute(sql, (new_id, user_id))
    conn.commit()

def delete_user(conn, user_id):
    user_id = str(user_id)
    with conn.cursor() as cursor:
        sql = "DELETE FROM test_tab WHERE id = %s;"
        cursor.execute(sql, (user_id,))
    conn.commit()
