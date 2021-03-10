import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="videotheque")
cursor=conn.cursor()

#2. Saisie des informations
nom = str(input('saisie nom: '))
prenom = str(input('saisie prenom: '))
mail = str(input('saisie mail: '))
mdp = str(input('saisie mdp: '))
movie = str(input('saisie film:'))

request5='select * from realisateur '
cursor.execute(request5)
realisateurs = cursor.fetchall()

request2='select * from film '
cursor.execute(request2)
films=cursor.fetchall()
#3. Création de la requete à partir des informations

#4. Envoi de la requete

#5. Traitement des résumtats
if (cursor.rowcount) > 0:
    for i in range(len(films)):
        nom_rea=""
        if movie in films[i][1]:
            id_rea=films[i][5]
            for j in range(len(realisateurs)):
                if id_rea in realisateurs[j]:
                    nom_rea=realisateurs[j][1]+' '+realisateurs[j][2]
            print(films[i][1]+', est realisé par: '+ nom_rea)
else:
    print("Aucun film trouvé")
#6. Fermeture de la BD
conn.close()