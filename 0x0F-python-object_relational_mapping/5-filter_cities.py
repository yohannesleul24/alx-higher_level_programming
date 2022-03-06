#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    Query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s;
    """
    stateName = sys.argv[4]
    c.execute(Query, (stateName,))
    [print(", ".join([city[0] for city in c.fetchall()]))]
    c.close()
    db.close()
