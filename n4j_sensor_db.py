import os
from py2neo import Graph
import pandas as pd
import functions as f


# Crea una connessione al database Neo4j locale
graph = Graph("bolt://localhost:7687", auth=("neo4j", "xxxxx"))

# query di popolamento
f.exequy("./query", graph)

# creazione nodi sensori fittizi via excel

# creazione df per i sensori

magnetic = "./input/sensors - magnetic.csv"
smart_plug = "./input/sensors - smartplug.csv"
gas = "./input/sensors - gas.csv"
temp = "./input/sensors - temp.csv"
movement = "./input/sensors - movement.csv"
light = "./input/sensors - light.csv"


csvs = [magnetic, smart_plug, gas, temp, movement, light]


# Itera sui df
for csv in csvs:

    df = pd.read_csv(csv)

    # Esegui la logica in base al file
    if csv == magnetic:
        label = "Magnetic_Sensor"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            state: row['state'],  
            timestamp: row['timestamp'], 
            type: row['type'], 
            room: row['room']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        #f.save_txt(label,query,"./output/")

    elif csv == smart_plug:
        label = "Smart_Plug"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            state: row['state'],
            voltage: row['voltage'],
            e_current: row['e_current'],
            active_power: row['active_power'],
            aparent_power: row['aparent_power'],
            reactive_power: row['reactive_power'],  
            timestamp: row['timestamp'], 
            type: row['type'], 
            floor: row['floor']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        #f.save_txt(label,query,"./output/")

    elif csv == gas:
        label = "Gas_Sensor"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            state: row['state'],  
            value: row['value'], 
            timestamp: row['timestamp'], 
            type: row['type'], 
            room: row['room']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        # f.save_txt(label,query,"./output/")

    elif csv == temp:
        label = "Temp_Sensor"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            temp: row['temp'],  
            humidity: row['humidity'], 
            timestamp: row['timestamp'], 
            type: row['type'], 
            room: row['room']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        # f.save_txt(label,query,"./output/")

    elif csv == movement:
        label = "Movement_Sensor"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            state: row['state'],  
            timestamp: row['timestamp'], 
            type: row['type'], 
            room: row['room']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        # f.save_txt(label,query,"./output/")

    elif csv == light:
        label = "Light_Sensor"

        # Crea i nodi per il file corrente
        query = """
            UNWIND $data as row
            CREATE (n:{label} {{id: row['id'],
            name: row['name'], 
            state: row['state'],  
            timestamp: row['timestamp'], 
            type: row['type'], 
            room: row['room']}})
            """
        query = query.format(label=label)
        graph.run(query, data=df.to_dict("records"))

        # salva su txt
        # f.save_txt(label,query,"./output/")


# creo le relazioni
f.exequy("./query/q_merge", graph)
