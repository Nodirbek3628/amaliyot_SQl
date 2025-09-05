from datetime import date

from psycopg2.pool import SimpleConnectionPool
import config

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host = config.DB_HOST,
    port = config.DB_PORT,
    user = config.DB_USER,
    password = config.DB_PASSWORD,
    dbname = config.DB_NAME)
conn = pool.getconn()
cur = conn.cursor()

cur.execute("""
    DROP TABLE IF EXISTS task;
""")


cur.execute("""
    CREATE TABLE task(
            id SERIAL PRIMARY KEY,
            title VARCHAR(64) NOT NULL,
            description TEXT,
            due_date DATE NOT NULL,
            created_at DATE NOT NULL
            
        );
    """)



due_date = date(year=2025, month=8, day=13)
today = date.today()

cur.execute("""
    INSERT INTO task(title, description, due_date, created_at)
            VALUES (%s, %s, %s, %s )
""",['Yugurish', 'Ertalab 3 km ',due_date,today ])

cur.execute("""
    INSERT INTO task(title, description, due_date, created_at)
            VALUES (%s, %s, %s, %s )
""",['kitob o\'qish ', 'Ertalab 3 soat ',due_date,today ])

cur.execute("SELECT * FROM task;")
rows = cur.fetchall()

for row in rows:
    id,title, desc, due, created = row
    print(id, title, due)


cur.close()

conn.commit()
conn.close()

pool.putconn(conn) # iwlatib bulib joyiga quyib quyish

