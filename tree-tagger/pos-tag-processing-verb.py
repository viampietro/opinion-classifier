import re
import subprocess

data_set_file = open("../data/dataset.csv", "r");
pos_tag_file = open("../data/lemmatized_data.csv", "a");


# lecture de chaque document contenu dans dataset.csv (un document = un commentaire)
for data_line in data_set_file :

    # envoi de la sortie de echo dans l'entree de tree-tager-english
    echo_stdout = subprocess.Popen(('echo', data_line), stdout=subprocess.PIPE)

    # tree_tagger_stdout est compose de lignes de la forme "MOT \t TAG \t LEMME \n"
    tree_tagger_stdout = subprocess.run(['tree-tagger-english', ''],
                                        stdin=echo_stdout.stdout,
                                        stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    # variable qui contient le document filtre par tree-tagger avant insertion
    # dans le fichier pos_tag.csv
    filtered_document = ""
    
    # lecture de chaque ligne de tree_tagger_stdout
    for tree_tagger_line in tree_tagger_stdout.split('\n') :
        
        # si la ligne eclatee en suivant les tabs contient 3 elements (MOT, TAG et LEMME)
        # on recupere le tag dans grammatical_category
        if (len(tree_tagger_line.split('\t')) == 3) :
            word = tree_tagger_line.split('\t')[0]
            lemma = tree_tagger_line.split('\t')[2]

            # si la categorie du mot est une des categories eligibles, contenue dans tags_list
            # on ecrit le mot dans le fichier pos_tag_verb.csv
            if (lemma != "<unknown>") :
                filtered_document += lemma + " "
            else :
                filtered_document += word + " "
                
    pos_tag_file.write(filtered_document + "\n")
    pos_tag_file.flush()    
    
    
    
    

