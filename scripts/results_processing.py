# Alexandre Culty (21508308)
# Maryam Soheili Majd (21613073) 
# Nicolas Delalande (20121972)
# Vincent Iampietro (20142295)

# PRE-REQUIS : results_file est un fichier contenant le resultat de
# classification de documents (une ligne = un document).
# Chaque ligne a pour syntaxe : inst#,actual,predicted,error,prediction
#
#
# PARAM :
# @results_file, chemin vers le document contenant les resultats d'une classification
# @expected_class, la classe attendue
#
# ACTION : calcule et affiche le nombre de documents bien classes dans results_file,
# en comparant la classe trouvee et la classe attendue.

def print_results (results_file, expected_class) :

    results = open(results_file + ".csv", "r", encoding="utf-8");

    number_of_documents = 0
    number_of_correctly_classified = 0;
    
    for result_line in results :

        # on recupere la classe trouvee
        found_class = result_line.split(',')[2].split(':')[1]

        if found_class == expected_class :
            number_of_correctly_classified += 1
            
        number_of_documents += 1
        
    accuracy = (number_of_correctly_classified * 100) / number_of_documents
    
    print(str(number_of_documents) + " documents, " + str(number_of_correctly_classified) + " correctly classified documents, " + str(accuracy) + "% accuracy.")

#
#
# ACTION : extraction des labels de classes d'un fichier de predictions
# de classes .csv
#
def extract_labels(source_file_name, destination_file_name) :

    source_file = open(source_file_name + ".csv", "r", encoding="utf-8");
    destination_file = open(destination_file_name + ".csv", "a", encoding="utf-8");
    
    for line in source_file :

        # on recupere la classe trouvee
        found_class = line.split(',')[2].split(':')[1]

        # ecriture du label dans le fichier de destination
        destination_file.write(found_class + "\n")
