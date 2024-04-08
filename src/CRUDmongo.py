from pymongo import MongoClient

client = MongoClient()
print(client)

db = client['pythonCrud']
print("Conexion exitosa")
while True:
    collection = db['crud']
    print("Seleccione la operacion a realizar")
    print("1. Insertar")
    print("2. Actualizar")
    print("3. Eliminar")
    print("4. Mostrar Todos")
    print("5. Buscar capitulo")
    print("6. Salir")

    switch = int(input("Ingrese la operacion a realizar: "))
    if switch == 1:
        unnamed = input("unnamed: ")
        print("rank: ")
        rank = input()
        trend = input("trend: ")
        season = input("season: ")
        episode = input("episode: ")
        name = input("name: ")
        start = input("start: ")
        total_votes = input("total_votes: ")
        average_rating = input("average_rating: ")
        try:
            db['crud'].insert_one({"unnamed": unnamed, "rank": rank, "trend": trend, "season": season, "episode": episode, "name": name, "start": start, "total_votes": total_votes, "average_rating": average_rating})
            print("Datos insertados correctamente")
        except Exception as e:
            print("Error: ", e)
    elif switch == 2:
        print("Actualizar")
        print("Numero del episodio: ")
        episode = int(input())
        print("Capitulo a actualizar: "+str(db['crud'].find_one({"episode": episode})))
        print("Nuevo ranking: ")
        rank = input()
        print("Nueva tendencia: ")
        trend = input()
        print("Nueva temporada: ")
        season = input()
        print("Nuevo nombre: ")
        name = input()
        print("Nuevo inicio: ")
        start = input()
        print("Nuevos votos: ")
        total_votes = input()
        print("Nuevo rating promedio: ")
        average_rating = input()

        try:
            db['crud'].update_one({"episode": episode}, {"$set": {"rank": rank, "trend": trend, "season": season, "name": name, "start": start, "total_votes": total_votes, "average_rating": average_rating}})

        except Exception as e:
            print("Error: ", e)

    elif switch == 3:
        print("Eliminar")
        episode = int(input("Numero del episodio: "))
        try:
            db['crud'].delete_one({"episode": episode})
            print("Datos eliminados correctamente")
        except Exception as e:
            print("Error: ", e)
    elif switch == 4:
        print("Mostrar Todos")
        datos = db['crud'].find()
        for dato in datos:
            print("\n\nEpisodio: "+str(dato["episode"])+"\nnombre: " + str(dato["name"])+"\nRanking: "+str(dato["rank"])+"\nrating: "+str(dato["average_rating"])+"\nVotos: "+str(dato["total_votes"])+"\nTendencia: "+str(dato["trend"])+"\nTemporada: "+str(dato["season"])+"\nInicio: "+str(dato["start"])+"\n")
    elif switch == 5:
        print("Buscar capitulo")
        episode = int(input("Numero del episodio: "))
        if db['crud'].find_one({"episode": episode}) is not None:
            dato = db['crud'].find_one({"episode": episode})
            print("\n\nEpisodio: "+str(dato["episode"])+"\nnombre: " + str(dato["name"])+"\nRanking: "+str(dato["rank"])+"\nrating: "+str(dato["average_rating"])+"\nVotos: "+str(dato["total_votes"])+"\nTendencia: "+str(dato["trend"])+"\nTemporada: "+str(dato["season"])+"\nInicio: "+str(dato["start"])+"\n")
        else:
            print("No se encontro el episodio")
    else:
        client.close()
        exit()

client.close()