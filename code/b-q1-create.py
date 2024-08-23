q1_create_cql = """
    CREATE TABLE IF NOT EXISTS session_items (
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        song_length float,
        PRIMARY KEY (session_id, item_in_session)
    )
"""
try:
    session.execute(q1_create_cql)
except Exception as e:
    print(e)
