q2_select_cql = """
    SELECT
        artist,
        song_title,
        user_first_name,
        user_last_name
    FROM user_sessions
    WHERE user_id = 10 AND session_id = 182
"""
try:
    q2_rows = session.execute(q2_select_cql)
except Exception as e:
    print(e)

for row in q2_rows:
    print((
        row.artist,
        row.song_title,
        row.user_first_name,
        row.user_last_name,
    ))
