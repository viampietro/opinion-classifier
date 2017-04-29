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
