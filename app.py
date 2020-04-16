import sqlite3
import pandas as pd

def connectDB():
    try:
        sqlcn = sqlite3.connect("data/data")
    except:
        print("Error loading database !")

    print("Database loaded successfully !")
    return sqlcn

def search(cn):
    print("Input parameter to search by :")
    p = input()
    
    print("Searching by" + " '" + p + "'" + ", enter search key :")
    s = input()

    try:
        df = pd.read_sql_query("SELECT * FROM people WHERE " + p + " = " "'" + s + "'",cn)
        print("______________________________")
        print(df)
    except:
        print("Non existent parameter !")
    


def main():
    conn = connectDB()
    print("______________________________")
    search(conn)


if __name__ == '__main__':
    main()