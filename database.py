import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user=input("user: "),
        password=input("password: "),
        database="mc_manager"
    )

def query(conn, sql, params=None):
    c = conn.cursor()
    try:
        c.execute(sql, params or ())
        conn.commit()
        print("ok")
    except Error as e:
        conn.rollback()
        raise e

def fetch(conn, sql, params=None):
    c = conn.cursor()
    c.execute(sql, params or ())
    rows = c.fetchall()
    cols = [d[0] for d in c.description]
    print("\n" + " | ".join(cols))
    print("-" * 60)
    for row in rows:
        print(" | ".join([str(v) if v is not None else "NULL" for v in row]))
    print()

# players

def add_player(conn, u, k):
    query(conn, "INSERT INTO Players (Username, Known_for) VALUES (%s, %s)", (u, k))

def update_player(conn, pid, u):
    query(conn, "UPDATE Players SET Username=%s WHERE id=%s", (u, pid))

def delete_player(conn, pid):
    query(conn, "DELETE FROM Players WHERE id=%s", (pid,))

def list_players(conn):
    fetch(conn, "SELECT * FROM Players")

# factions

def add_faction(conn, name, owner):
    query(conn, "INSERT INTO Factions (Name, Owner) VALUES (%s, %s)", (name, owner))

def update_faction(conn, fid, name, owner):
    query(conn, "UPDATE Factions SET Name=%s, Owner=%s WHERE id=%s", (name, owner, fid))

def delete_faction(conn, fid):
    query(conn, "DELETE FROM Factions WHERE id=%s", (fid,))

def list_factions(conn):
    fetch(conn, "SELECT * FROM Factions")

# memberships

def add_membership(conn, pid, fid):
    query(conn, "INSERT INTO Faction_Memberships (Player_id, Faction_id) VALUES (%s, %s)", (pid, fid))

def delete_membership(conn, mid):
    query(conn, "DELETE FROM Faction_Memberships WHERE id=%s", (mid,))

def list_memberships(conn):
    fetch(conn, "SELECT fm.id, p.Username, f.Name FROM Faction_Memberships fm JOIN Players p ON fm.Player_id=p.id JOIN Factions f ON fm.Faction_id=f.id")

# bases

def add_base(conn, name, owner, faction):
    query(conn, "INSERT INTO Bases (Name, Owner, Faction) VALUES (%s, %s, %s)", (name, owner, faction))

def update_base(conn, bid, name, owner, faction):
    query(conn, "UPDATE Bases SET Name=%s, Owner=%s, Faction=%s WHERE id=%s", (name, owner, faction, bid))

def delete_base(conn, bid):
    query(conn, "DELETE FROM Bases WHERE id=%s", (bid,))

def list_bases(conn):
    fetch(conn, "SELECT * FROM Bases")

# shops

def add_shop(conn, owner, name, product):
    query(conn, "INSERT INTO Shops (Owner, Name, product) VALUES (%s, %s, %s)", (owner, name, product))

def update_shop(conn, sid, owner, name, product):
    query(conn, "UPDATE Shops SET Owner=%s, Name=%s, product=%s WHERE id=%s", (owner, name, product, sid))

def delete_shop(conn, sid):
    query(conn, "DELETE FROM Shops WHERE id=%s", (sid,))

def list_shops(conn):
    fetch(conn, "SELECT * FROM Shops")

# events

def add_event(conn, owner, name, desc, date):
    query(conn, "INSERT INTO Events (Owner, Name, description, date) VALUES (%s, %s, %s, %s)", (owner, name, desc, date))

def update_event(conn, eid, name, desc, date):
    query(conn, "UPDATE Events SET Name=%s, description=%s, date=%s WHERE id=%s", (name, desc, date, eid))

def delete_event(conn, eid):
    query(conn, "DELETE FROM Events WHERE id=%s", (eid,))

def list_events(conn):
    fetch(conn, "SELECT * FROM Events")
