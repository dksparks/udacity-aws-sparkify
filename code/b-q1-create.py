q1_create_cql = """
    -- This table tracks song information, organized
    -- as items within individual listening sessions.
    -- The session_id is used as the partition key
    -- to distribute data across nodes,
    -- and item_in_session is used as the
    -- clustering column to sort the result.
    CREATE TABLE IF NOT EXISTS session_items (
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        song_length float,
        PRIMARY KEY ((session_id), item_in_session)
    )
"""
try:
    session.execute(q1_create_cql)
except Exception as e:
    print(e)
