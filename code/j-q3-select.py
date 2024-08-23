q3_select_cql = """
    SELECT
        user_first_name,
        user_last_name
    FROM song_listeners 
    WHERE song_title = 'All Hands Against His Own'
"""
try:
    q3_rows = session.execute(q3_select_cql)
except Exception as e:
    print(e)

for row in q3_rows:
    print((row.user_first_name, row.user_last_name))
