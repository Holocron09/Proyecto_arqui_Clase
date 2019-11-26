import psycopg2
conn=psycopg2.connect('dbname=pi')
cur=conn.cursor()
cur.execute('select * from personas')
results=cur.fetchall()
for result in results:
    print(result)