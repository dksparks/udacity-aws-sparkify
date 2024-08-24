q3_create_cql = """
    -- This table tracks users who have listened
    -- to each song. The song_title is used as the 
    -- partition key to distribute data across nodes, 
    -- and user_id is used as the clustering column 
    -- to sort the result.
    CREATE TABLE IF NOT EXISTS song_listeners (
        song_title text,
        user_id int,
        user_first_name text,
        user_last_name text,
        -- Note: This primary key may not be unique
        -- across the entire dataset, because it is
        -- possible for a user to listen to a song
        -- more than once. Specifying the primary key
        -- in this manner will lead to users appearing
        -- only once in the results for a song, even
        -- if they listened to it more than once,
        -- since any further rows for that user-song
        -- pair will overwrite the first one upon
        -- insertion. It is not clear from the project
        -- guidelines whether or not this is the
        -- desired behavior.
        PRIMARY KEY ((song_title), user_id)
    )
"""
try:
    session.execute(q3_create_cql)
except Exception as e:
    print(e)
