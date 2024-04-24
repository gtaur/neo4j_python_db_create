import functions as f
from py2neo import Graph

# Crea una connessione al database Neo4j locale
graph = Graph("bolt://localhost:7687", auth=("neo4j", "xxxxx"))

# PER LA CREAZIONE DEL GRAFO ESEGUIRE LO SCRIPT N4J_SENSOR_DB

# uso il main solo per resettare il db in caso di errori
# pulisci il grafo
f.exequy("./query/q_delete", graph)

