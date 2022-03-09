import mysql.connector

def databaseConnexion():
  try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="cngdatabase")
  except:
    # Connexion to MySQL
    mydb = mysql.connector.connect(host="localhost", user="root", password="")
    mycursor = mydb.cursor()
    print("Connecté au server Mysql !")

    # Create Database if not exists
    mycursor.execute("CREATE DATABASE cngdatabase")
    print("Base de donnée CNG Database créée")
    mydb.close()
    print("Connexion réinitialisée")

    # New Connexion
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="cngdatabase")
    mycursor = mydb.cursor()
    print("Nouvelle Connexion")

    # Create Administration
    sql = "CREATE TABLE administration (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, username VARCHAR(70) NOT NULL, password VARCHAR(70) NOT NULL)"
    mycursor.execute(sql)
    print("Table administrateur créée !")

     # Create Lutteur
    sql = "CREATE TABLE lutteur (pseudo VARCHAR(40) NOT NULL PRIMARY KEY, ecurie VARCHAR(40) NOT NULL, nom VARCHAR(40) NOT NULL,  prenom VARCHAR(40) NOT NULL, ddn DATE NOT NULL, nbr_combat INT NOT NULL, nbr_victoire INT NOT NULL, nbr_nul INT NOT NULL)"
    mycursor.execute(sql)
    print("Table Lutteur créée !")

    # Insert Defaul admin
    sql = "INSERT INTO administration (username, password) VALUES (%s, %s)"
    values = ("root", "root")
    mycursor.execute(sql, values)
    mydb.commit()
    print("Utilisateur Par défaut Root insérée!")
    
  
  return mydb
