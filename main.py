import database as db
from mysql.connector import Error

def run_menu(title, options):
    while True:
        print(f"\n{title}")
        for k, (label, _) in options.items():
            print(f"  {k}. {label}")
        print("  0. back")
        choice = input("> ").strip()
        if choice == "0":
            break
        elif choice in options:
            try:
                options[choice][1]()
            except Error as e:
                print(f"error: {e}")
            except ValueError as e:
                print(f"invalid input: {e}")
        else:
            print("?")

def require_int(prompt):
    val = input(prompt).strip()
    if not val.isdigit():
        raise ValueError(f"'{val}' is not a valid ID")
    return val

def require_str(prompt, max_len=None):
    val = input(prompt).strip()
    if not val:
        raise ValueError("field cannot be empty")
    return val[:max_len] if max_len else val

# players

def players_menu(conn):
    run_menu("players", {
        "1": ("list",   lambda: db.list_players(conn)),
        "2": ("add",    lambda: add_player(conn)),
        "3": ("update", lambda: update_player(conn)),
        "4": ("delete", lambda: delete_player(conn)),
    })

def add_player(conn):
    u = require_str("username: ", max_len=16)
    k = input("known for: ").strip()
    db.add_player(conn, u, k)

def update_player(conn):
    pid = require_int("player id: ")
    u = require_str("new username: ", max_len=16)
    db.update_player(conn, pid, u)

def delete_player(conn):
    pid = require_int("player id: ")
    if input(f"delete player {pid}? y/n: ") == "y":
        db.delete_player(conn, pid)

# factions

def factions_menu(conn):
    run_menu("factions", {
        "1": ("list",   lambda: db.list_factions(conn)),
        "2": ("add",    lambda: add_faction(conn)),
        "3": ("update", lambda: update_faction(conn)),
        "4": ("delete", lambda: delete_faction(conn)),
    })

def add_faction(conn):
    name = require_str("name: ")
    owner = require_int("owner player id: ")
    db.add_faction(conn, name, owner)

def update_faction(conn):
    fid = require_int("faction id: ")
    name = require_str("new name: ")
    owner = require_int("new owner player id: ")
    db.update_faction(conn, fid, name, owner)

def delete_faction(conn):
    fid = require_int("faction id: ")
    if input(f"delete faction {fid}? y/n: ") == "y":
        db.delete_faction(conn, fid)

# memberships

def memberships_menu(conn):
    run_menu("memberships", {
        "1": ("list",   lambda: db.list_memberships(conn)),
        "2": ("add",    lambda: add_membership(conn)),
        "3": ("delete", lambda: delete_membership(conn)),
    })

def add_membership(conn):
    pid = require_int("player id: ")
    fid = require_int("faction id: ")
    db.add_membership(conn, pid, fid)

def delete_membership(conn):
    mid = require_int("membership id: ")
    db.delete_membership(conn, mid)

# bases

def bases_menu(conn):
    run_menu("bases", {
        "1": ("list",   lambda: db.list_bases(conn)),
        "2": ("add",    lambda: add_base(conn)),
        "3": ("update", lambda: update_base(conn)),
        "4": ("delete", lambda: delete_base(conn)),
    })

def add_base(conn):
    name = require_str("name: ")
    owner = input("owner player id (blank=none): ").strip() or None
    faction = input("faction id (blank=none): ").strip() or None
    db.add_base(conn, name, owner, faction)

def update_base(conn):
    bid = require_int("base id: ")
    name = require_str("new name: ")
    owner = input("owner player id (blank=none): ").strip() or None
    faction = input("faction id (blank=none): ").strip() or None
    db.update_base(conn, bid, name, owner, faction)

def delete_base(conn):
    bid = require_int("base id: ")
    if input(f"delete base {bid}? y/n: ") == "y":
        db.delete_base(conn, bid)

# shops

def shops_menu(conn):
    run_menu("shops", {
        "1": ("list",   lambda: db.list_shops(conn)),
        "2": ("add",    lambda: add_shop(conn)),
        "3": ("update", lambda: update_shop(conn)),
        "4": ("delete", lambda: delete_shop(conn)),
    })

def add_shop(conn):
    owner = input("owner player id (blank=none): ").strip() or None
    name = require_str("shop name: ")
    product = require_str("product: ")
    db.add_shop(conn, owner, name, product)

def update_shop(conn):
    sid = require_int("shop id: ")
    owner = input("owner player id (blank=none): ").strip() or None
    name = require_str("new name: ")
    product = require_str("new product: ")
    db.update_shop(conn, sid, owner, name, product)

def delete_shop(conn):
    sid = require_int("shop id: ")
    if input(f"delete shop {sid}? y/n: ") == "y":
        db.delete_shop(conn, sid)

# events

def events_menu(conn):
    run_menu("events", {
        "1": ("list",   lambda: db.list_events(conn)),
        "2": ("add",    lambda: add_event(conn)),
        "3": ("update", lambda: update_event(conn)),
        "4": ("delete", lambda: delete_event(conn)),
    })

def add_event(conn):
    owner = input("owner player id (blank=none): ").strip() or None
    name = require_str("name: ")
    desc = input("description: ").strip()
    date = require_str("date (YYYY-MM-DD HH:MM:SS): ")
    db.add_event(conn, owner, name, desc, date)

def update_event(conn):
    eid = require_int("event id: ")
    name = require_str("new name: ")
    desc = input("new description: ").strip()
    date = require_str("new date (YYYY-MM-DD HH:MM:SS): ")
    db.update_event(conn, eid, name, desc, date)

def delete_event(conn):
    eid = require_int("event id: ")
    if input(f"delete event {eid}? y/n: ") == "y":
        db.delete_event(conn, eid)

# main

def main():
    try:
        conn = db.get_connection()
    except Error as e:
        print(f"couldn't connect: {e}")
        return

    run_menu("mc manager", {
        "1": ("players",     lambda: players_menu(conn)),
        "2": ("factions",    lambda: factions_menu(conn)),
        "3": ("memberships", lambda: memberships_menu(conn)),
        "4": ("bases",       lambda: bases_menu(conn)),
        "5": ("shops",       lambda: shops_menu(conn)),
        "6": ("events",      lambda: events_menu(conn)),
    })

    conn.close()

if __name__ == "__main__":
    main()
