from fastapi import FastAPI
import sqlite3
from sqlalchemy import create_engine, Table, select, MetaData





sqlite_db = "testdb.db"
conn = sqlite3.connect(sqlite_db)
# cur = conn.execute("select * from TestResult")
# print(cur.fetchall())



# create_table ="""CREATE TABLE TestResult (
# id integer PRIMARY KEY,
# pathogen TEXT,
# patient_name TEXT
# );"""

# insert_results = """INSERT INTO TestResult VALUES 
#     (1, "COVID", "P_1"), 
#     (2, "COVID", "P_2"), 
#     (3, "RSV", "P_3"), 
#     (4, "RSV", "P_4")
# """

# with sqlite3.connect(sqlite_db) as conn:
#     cursor = conn.cursor()
#     cursor.execute(create_table)
#     cursor.execute(insert_results)
#     conn.commit()



app = FastAPI()

DATABASE_URL = "sqlite:///testdb.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
table_name = 'TestResult'

@app.get("/")
def home():
    return {"message": "My Project"}

@app.get("/testresults")
def test_results():
    conn = sqlite3.connect(sqlite_db)
    result  = conn.execute("select * from TestResult").fetchall()
    conn.close()

    return [dict(r) for r in result]


