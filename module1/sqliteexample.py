import sqlite3
import queries as q # this is where you can save all queries and call them here)

# step 1 - connect to database
# if misspelled or db isn't there, it'll default to creating a new one
'''connection = sqlite3.connect('rpg_db.sqlite3')'''

# step 2 - create a cursor (a 'middleman' to make changes to db without ruining it)
'''cursor = connection.cursor()'''

# step 3 - write a query 
# semicolon punctuates SQL varchar (varchar = strings) but isn't mandatory to run, best practice to use for multiple varchar queries
'''query = 'SELECT character_id, name FROM charactercreator_character;'''

# step 4 - execute query on cursor to fetch, or pull, results
'''results = cursor.execute(q.SELECTALL).fetchall()'''


#step 5 - create 'if name main' statement to print query fetch
'''if __name__ == '__main__':
    print(results[:5])'''

# IMPROVED 'PIPELINE'

def dbconnect(name='rpg_db.sqlite3'):
    return sqlite3.connect(name)    

def qexecute(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()

if __name__ == '__main__':
    conn = dbconnect()
    print(qexecute(conn, q.SELECTALL)[:5])
    print()
    print(qexecute(conn, q.JOINMAGE)[:5])