file = 'event_datafile_new.csv'
with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader) # skip header
    # partial query string does not depend on line,
    # so it can be moved outside the for loop
    q1_insert_cql = """
        INSERT INTO session_items (
            session_id,
            item_in_session,
            artist,
            song_title,
            song_length
        ) VALUES (%s, %s, %s, %s, %s)
    """
    for line in csvreader:
        try:
            session.execute(q1_insert_cql, (
                int(line[8]),
                int(line[3]),
                line[0],
                line[9],
                float(line[5]),
            ))
        except Exception as e:
            print(e)
