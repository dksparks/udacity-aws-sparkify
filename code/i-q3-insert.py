file = 'event_datafile_new.csv'
with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader) # skip header
    # partial query string does not depend on line,
    # so it can be moved outside the for loop
    q3_insert_cql = """
        INSERT INTO song_listeners (
            song_title,
            user_id,
            user_first_name,
            user_last_name
        ) VALUES (%s, %s, %s, %s)
    """
    for line in csvreader:
        try:
            session.execute(q3_insert_cql, (
                line[9],
                int(line[10]),
                line[1],
                line[4],
            ))
        except Exception as e:
            print(e)
