q2_create_cql = """
    -- This table tracks user and song information, 
    -- organized by individual listening sessions.
    -- The user_id and session_id are used as a 
    -- composite partition key to distribute data 
    -- across nodes, and item_in_session is used as 
    -- the clustering column to sort the result.
    CREATE TABLE IF NOT EXISTS user_sessions (
        user_id int,
        session_id int,
        item_in_session int,
        artist text,
        song_title text,
        user_first_name text,
        user_last_name text,
        PRIMARY KEY (
            (user_id, session_id),
            item_in_session
        )
    )
"""
try:
    session.execute(q2_create_cql)
except Exception as e:
    print(e)
