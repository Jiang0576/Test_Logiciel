import sqlite3
import json

# Connectez-vous à la base de données, le fichier de base de données existe dans ce répertoire
conn = sqlite3.connect('practice2.sqlite3')
cur = conn.cursor()

def check_username(username):
    # Vérifier le format du nom d'utilisateur
    if type(username) != str:
        return False
    if len(username) <= 3:
        return False
    return username.isalnum()

def check_password(password):
    # Vérifier le format du mot de passe
    if type(password) != str:
        return False
    if len(password) < 8:
        return False
    upper, special, number, standard = False, False, False, False
    for i in range(len(password)):
        if password[i].isupper() == True:
            upper = True
        if password[i].isalnum() == False:
            special = True
        if password[i].isdigit() == True:
            number = True
        if password[i].isalnum() == True:
            standard =True
    return upper and special and number and standard

def check_link(link):
    # vérifier le format du lien
    if type(link) != list:
        return False
    for string in link:
        if not string.isalnum():
            return False
    return True

def create_table():
    # Créer des tables de base de données
    sql = """CREATE TABLE user(username varchar(15) primary key, password varchar(15), link varchar(150));"""
    cur.execute(sql)

def insert_data(username, password):
    # Insérez le nom d'utilisateur et le mot de passe, pas de contrôle de format ici
    sql = """insert into user(username, password) values('{0}', '{1}');""".format(username, password)
    cur.execute(sql)

def check_pair(username, password):
    # Vérifiez le format du nom d'utilisateur et du mot de passe et vérifiez si ces données existent dans la base de données
    if not check_username(username) or not check_password(password):
        return False
    sql = """SELECT * FROM user WHERE username = '{0}' and password = '{1}';""".format(username, password)
    cur.execute(sql)
    result = cur.fetchone()
    if result == None:
        return False
    return True

def update_link(username, password, link):
    # Ajouter un lien vers l'utilisateur
    sql = """update user set link = '{2}' where username = '{0}' and password = '{1}';""".format(username, password, json.dumps(link))
    cur.execute(sql)

def get_link(username, password):
    # Obtenir le lien utilisateur
    sql = """SELECT * FROM user WHERE username = '{0}' and password = '{1}';""".format(username, password)
    cur.execute(sql)
    result = cur.fetchone()
    link = json.loads(result[0][2])
    return link

def check_database():
    # Vérifiez que toutes les données de la base de données sont conformes au format
    sql = """SELECT * FROM user ;"""
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        username = row[0]
        password = row[1]
        link = json.loads(row[2])
        if not check_username(username) or not check_password(password) or not check_link(link):
            return False
    return True

# Créer une table de données, ignorer si déjà créé
try:
    create_table()
except:
    pass