q3_create_cql = """
    CREATE TABLE IF NOT EXISTS song_listeners (
        song_title text,
        session_id int,
        item_in_session int,
        user_first_name text,
        user_last_name text,
        PRIMARY KEY (
            song_title,
            session_id,
            item_in_session
        )
    )
"""
try:
    session.execute(q3_create_cql)
except Exception as e:
    print(e)
