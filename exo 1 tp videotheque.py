import mysql.connector

#1. Connexion à la BD
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="videotheque2")

#2. Saisie des informations
mail = str(input('saisie mail: '))
mdp = str(input('saisie mdp: '))

#3. Création de la requete à partir des informations
req = "SELECT * FROM user"

#4. Envoi de la requete
cursor = conn.cursor()
cursor.execute(req)

#5. Traitement des résultats
tab = cursor.fetchall()
if (cursor.rowcount) > 0:
    for ligne in tab:
        if mail in ligne and mdp in ligne:
            print("Bonjour " + ligne[1] + " " + ligne[2])
else:
    print ("Personne inconnue")

#6. Fermeture des résultats
conn.close()