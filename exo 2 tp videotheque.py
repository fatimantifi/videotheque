import mysql.connector

#1. Connexion à la BD
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="videotheque2")

#2. Saisie des informations
nom = str(input('saisie nom: '))
prenom = str(input('saisie prenom: '))
mail = str(input('saisie mail: '))
mdp = str(input('saisie mdp: '))

#3. Création de la requete à partir des informations
req = "INSERT INTO user (nom, prenom, mail, mdp) VALUES ('"+nom+"', '"+prenom+"', '"+mail+"', '"+mdp+"')"
#print(req)
print(req)

#4. Envoi de la requete
cursor = conn.cursor()
cursor.execute(req)
conn.commit()

#5. Traitement des résumtats
if(cursor.rowcount > 0):
    print("Ajout réussi")
else:
    print("Erreur lors de l'ajout")

#6. Fermeture des résultats
conn.close()
