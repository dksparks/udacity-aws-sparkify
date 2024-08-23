file = 'event_datafile_new.csv'
with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader) # skip header
    # partial query string does not depend on line,
    # so it can be moved outside the for loop
    q2_insert_cql = """
        INSERT INTO user_sessions (
            user_id,
            session_id,
            item_in_session,
            artist,
            song_title,
            user_first_name,
            user_last_name
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for line in csvreader:
        try:
            session.execute(q2_insert_cql, (
                int(line[10]),
                int(line[8]),
                int(line[3]),
                line[0],
                line[9],
                line[1],
                line[4],
            ))
        except Exception as e:
            print(e)
