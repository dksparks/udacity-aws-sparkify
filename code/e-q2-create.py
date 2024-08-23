q2_create_cql = """
    CREATE TABLE IF NOT EXISTS user_sessions (
        user_id int,
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        user_first_name text,
        user_last_name text,
        PRIMARY KEY (
            user_id,
            session_id,
            item_in_session
        )
    )
"""
try:
    session.execute(q2_create_cql)
except Exception as e:
    print(e)
