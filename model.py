#project model
import sqlite3
def get_country():
    countries = []
    with sqlite3.connect('application.db') as con:
        stmt = 'select countries from country'
        rs = con.execute(stmt)
    for country in rs.fetchall():
        for con in country:
            countries.append(con)
    return countries
#print(get_country())
import sqlite3
import random


def fetch_teams():
    """Fetch team names from the database."""
    conn = sqlite3.connect('application.db')
    c = conn.cursor()
    c.execute('SELECT countries FROM country')
    teams = [row[0] for row in c.fetchall()]
    conn.close()
    return teams


def generate_fixtures():
    """Generate random fixtures from the list of teams."""
    teams = fetch_teams()
    random.shuffle(teams)  # Shuffle the team list
    fixtures = []
    for i in range(0, len(teams), 2):
        try:
            fixtures.append(f'{teams[i]} vs {teams[i + 1]}')
        except IndexError:
            fixtures.append(f'{teams[i]} has a bye')

    return fixtures
def convertToBinaryData(filename):
    # Convert binary format to images
    # or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def login_check():
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        rs = cursor.execute("SELECT username,password from admin")
        rs_list = list(rs.fetchall())
        print(rs_list)

def get_fixtures():
    score = 0
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        rs = cursor.execute(f"SELECT ID,Team1,Score1,Team2,Score2 FROM FIXTURES WHERE Score1 == '' ")
        rs_list = list(rs.fetchall())
        return rs_list
def get_ac_fixtures():
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        rs = cursor.execute(f"SELECT ID,Date,Team1,Score1,Team2,Score2 FROM FIXTURES WHERE Score1 == '' ")
        rs_list = list(rs.fetchall())
        return rs_list
def update_fix_table(id,score1,score2):
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE FIXTURES SET Score1 = :score1, Score2 = :score2 WHERE ID = :id",{'score1':score1,'score2':score2,'id':id})

        conn.commit()
def add_to_leader_board(name,point):
    with sqlite3.connect('application.db') as con:
        cursor = con.cursor()

        table_query = '''CREATE TABLE IF NOT EXISTS
                               leader_board (ID INTEGER primary key autoincrement,Team TEXT, Point NUMERIC
                               )'''

        con.execute(table_query)
        try:
            cursor.execute('''insert into leader_board (Team,Point) Values(?,?)
                                                 ''', (name,point))
        except:
            print('already exists')

        con.commit()
def add_point(point,name):
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        rs = cursor.execute("SELECT Point FROM leader_board WHERE Team = :name",{'name':name})
        points = [row[0] for row in rs.fetchall()]
        new_point = points[0] + point
        cursor.execute("UPDATE leader_board SET Point = :new_point WHERE Team = :name",{'new_point':new_point,'name':name})

        conn.commit()

def get_leader_board():
    with sqlite3.connect('application.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute("SELECT Team, Point FROM leader_board ORDER BY Point DESC")

        return result.fetchall()

def admin_info(username,password):
    with sqlite3.connect('application.db') as con:
        cursor = con.cursor()
        query = 'CREATE TABLE IF NOT EXISTS admin(username TEXT NOT NULL, password TEXT primary key)'
        con.execute(query)

        try:
            cursor.execute('insert into admin(username,password)  values(?,?)',(username,password))
        except:
            print('exists')

        con.commit()
admin_info('Basketballadmin','IntBball.@admin')
#print(get_leader_board())
#print(get_fixtures())
print(get_ac_fixtures())
#login_check()
# print(fetch_teams())
# print(generate_fixtures())
#['Ghana vs Nigeria', "Guinea vs Cote d'voire", 'Niger vs Cameroon', 'Benin Republic vs Kenya']