import sqlite3

def databaseConnexion():
  mydb = sqlite3.connect('../cngdatabase.db')
  mycursor = mydb.cursor()
  sql = "CREATE TABLE IF NOT EXISTS administration (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, UNIQUE(username))"
  mycursor.execute(sql)

  sql = "CREATE TABLE IF NOT EXISTS lutteur (pseudo TEXT NOT NULL PRIMARY KEY, ecurie TEXT NOT NULL, nom TEXT NOT NULL,  prenom TEXT NOT NULL, ddn TEXT NOT NULL, nbr_combat INTEGER NOT NULL, nbr_victoire INTEGER NOT NULL, nbr_nul INTEGER NOT NULL)"
  mycursor.execute(sql)

  mycursor.execute("SELECT * FROM administration WHERE username=:username", {"username":"root"})
  user = mycursor.fetchone()

  if user == None:
    sql = "INSERT INTO administration (username, password) VALUES (:username, :password)"
    values = {"username": "root", "password":"root"}
    mycursor.execute(sql, values)
    mydb.commit()    
  
  return mydb
