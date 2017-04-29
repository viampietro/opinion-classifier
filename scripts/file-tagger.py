import re
import subprocess

#
# PRE-REQUIS :
# 1. se placer dans le dossier du data_file specifie.
# 2. data_file doit etre une fichier texte.
# 3. le dossier bin et cmd du tree-tagger doivent etre ajoutes au PATH
#
# PARAM :
# @data_file, le fichier source a tagger.
# @target_tagged_file, le fichier destination tagge.
# @tags_list, une liste de tags, categories grammaticales qui ne seront pas filtrees
# par la procedure.
#
# ACTION : Ne garde que les mots dont le type grammatical est reference dans tags_list
# et remplace les mots selectionnes par leur lemme (si il en existe).
# Si tags_list est vide, alors la procedure tag_file conserve tous les mots.
# 

# Quelques tags_list :
# ['JJ', 'JJR', 'JJS'], pour ne garder que les adjectifs 
#  

def tag_file (data_file, target_tagged_file, tags_list=[]) :

    data_set_file = open(data_file + ".csv", "r");
    tagged_file = open(target_tagged_file + ".csv", "a");
    

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
                grammatical_category = tree_tagger_line.split('\t')[1]
                lemma = tree_tagger_line.split('\t')[2]

                # si tags_list est vide ou si le mot a une categorie grammaticale eligible
                if (not tags_list) or (grammatical_category in tags_list) :

                    # on ecrit le mot dans le fichier target.csv
                    if (lemma != "<unknown>") :
                        filtered_document += lemma + " "
                    else :
                        filtered_document += word + " "
                    
        tagged_file.write(filtered_document + "\n")
        tagged_file.flush()    

        
    
    
    

