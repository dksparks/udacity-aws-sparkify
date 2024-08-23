q1_select_cql = """
    SELECT artist, song_title, song_length
    FROM session_items
    WHERE session_id = 338 AND item_in_session = 4
"""
try:
    q1_rows = session.execute(q1_select_cql)
except Exception as e:
    print(e)

for row in q1_rows:
    print((
        row.artist,
        row.song_title,
        row.song_length,
    ))
