try:
    session.execute('DROP TABLE session_items')
except Exception as e:
    print(e)

try:
    session.execute('DROP TABLE user_sessions')
except Exception as e:
    print(e)

try:
    session.execute('DROP TABLE song_listeners')
except Exception as e:
    print(e)
