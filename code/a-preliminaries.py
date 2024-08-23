try:
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkify
        WITH REPLICATION = {
            'class' : 'SimpleStrategy',
            'replication_factor' : 1 
        }
    """)
except Exception as e:
    print(e)

###
###
###

try:
    session.set_keyspace('sparkify')
except Exception as e:
    print(e)
