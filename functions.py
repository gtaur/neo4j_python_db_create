import os

# esecuzione query da file di texto

def exequy(direc,graph):

    # Itera sui file nella directory
    for filename in os.listdir(direc):
        # Verifica se il file è un file di testo
        if filename.endswith(".txt"):
            # Percorso completo del file
            filepath = os.path.join(direc, filename)

            # Leggi il contenuto del file di testo
            with open(filepath, "r") as file:
                query_string = file.read()

            # Esegui la query su Neo4j
            result = graph.run(query_string)

            # Mostra l'output della query in console
            print(f"Risultato della query per il file: {filename}")
            for record in result:
                print(record)
            print("------------------------------------")


def save_txt(label,query,in_dir):
    testo = in_dir + label + '.txt'
    with open(testo,'w' ) as file:
        file.write(query)
        print("Scrittura" + testo + "completata con successo.")