import mysql.connector

#1. Connexion à la BD
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="videotheque2")

#2. Saisie des informations
nom = str(input('saisie nom: '))
prenom = str(input('saisie prenom: '))
mail = str(input('saisie mail: '))
mdp = str(input('saisie mdp: '))
movie = str(input('saisie film:'))

#3. Création de la requete à partir des informations
req = "SELECT titre FROM film"
#print(req)
print(req)
#4. Envoi de la requete
cursor = conn.cursor()
cursor.execute(req,movie)

#5. Traitement des résumtats
tab = cursor.fetchall()
if (cursor.rowcount) > 0:
    for ligne in tab:
        if movie in ligne[0]:
            print(ligne)
            print ("- "+ligne[0])
else:
    print("Aucun film trouvé")

#6. Fermeture des résultats
conn.close()