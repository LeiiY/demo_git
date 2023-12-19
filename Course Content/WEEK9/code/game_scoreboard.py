import sqlite3

def create_db():
    conn = sqlite3.connect('game.db')
    try:
        conn.execute('CREATE TABLE SCOREBOARD (NAME TEXT, SCORE INT);')
    except:
        pass
    conn.close()

def log_score(name, score):
    conn = sqlite3.connect('game.db')
    conn.execute("INSERT INTO SCOREBOARD (NAME, SCORE) VALUES ('{}', {});".format(name, score))
    conn.commit()
    conn.close()

def get_top_scores():
    conn = sqlite3.connect('game.db')
    rows = conn.execute('SELECT * FROM SCOREBOARD ORDER BY SCORE DESC LIMIT 2;')
    print('Top two scores:')
    for row in rows:
        print(row)
    conn.close()

create_db()
log_score('Fred Bloggs', 12800)
log_score('Susan Smith', 28250)
log_score('Abdul Kalam', 14300)
get_top_scores()
