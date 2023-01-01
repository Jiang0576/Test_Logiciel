from practice2 import *

def test_check_username():
    assert check_username(1) == False
    assert check_username("asd") == False
    assert check_username("Jackson") == True
    assert check_username("Lucy!") == False

def test_check_password():
    assert check_password(1) == False
    assert check_password("asdfghj") == False
    assert check_password("asdfGH1!") == True
    assert check_password("asdfGG!!") == False

def test_check_link():
    assert check_link(["link1"]) == True
    assert check_link(["link1", "link2!!"]) == False

def test_insert_data():
    sql = """SELECT * FROM user ;"""
    cur.execute(sql)
    assert cur.fetchall() == []
    insert_data("user1", "asdxzcA!1")
    cur.execute(sql)
    result = cur.fetchall()
    assert result == [('user1', 'asdxzcA!1', None)]
    conn.rollback()

def test_check_pair():
    assert check_pair("user1", "asdxzcA!1") == False
    insert_data("user1", "asdxzcA!1")
    insert_data("user2", "asdxzcA!a")
    assert check_pair("user1", "asdxzcA!1") == True
    assert check_pair("user2", "asdxzcA!a") == False
    conn.rollback()

def test_update_link_and_get_link():
    insert_data("user1", "asdxzcA!1")
    link = ["asdadxzc", "sadwqdqqrf"]
    assert get_link("user1", "asdxzcA!1") == None
    update_link("user1", "asdxzcA!1", link)
    assert get_link("user1", "asdxzcA!1") == link
    conn.rollback()

def test_check_database():
    insert_data("user1", "asdxzcA!1")
    insert_data("user2", "asdxzcB%2")
    assert check_database() == True
    link = ["asdadxzc", "sadwqdqqrf"]
    update_link("user1", "asdxzcA!1", link)
    assert check_database() == True
    insert_data("user3", "asdxzcAAA")
    assert check_database() == False
    conn.rollback()