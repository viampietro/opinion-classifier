import re
import subprocess
import pprint
import treetaggerwrapper

####################### !!!! POUR FAIRE MARCHER TAG_FILE !!!! #########################
#
# Il faut installer le wrapper python pour tree-tagger :
#
# 1. Installer le module treetaggerwrapper :
#    (il peut etre necessaire d'installer le module setuptools : pip install setuptools)
#    pip install treetaggerwrapper OU pip3 install treetaggerwrapper
#
# 2. Mettre le dossier treetagger contenant les executables dans votre dossier /home
# pour que le module treetaggerwrapper le detecte
# ex : /home/treetagger
########################################################################################

########################################################################################
# PRE-REQUIS : source_file doit etre une fichier texte.
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

def tag_file (source_file_name, destination_file_name, tags_list=[]) :

    # objet TreeTagger
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en')

    source_file = open(source_file_name + ".csv", "r");
    destination_file = open(destination_file_name + ".csv", "a");
    

    # lecture de chaque document contenu dans dataset.csv (un document = un commentaire)
    for document in source_file :

        tagger_output = tagger.tag_text(document)
        
        # variable qui contient le document filtre par tree-tagger avant insertion
        # dans le fichier pos_tag.csv
        filtered_document = ""

        # lecture de chaque ligne de tree_tagger_stdout
        for tag in tagger_output :
        
            # si la ligne eclatee en suivant les tabs contient 3 elements (MOT, TAG et LEMME)
            # on recupere le tag dans grammatical_category
            if (len(tag.split('\t')) == 3) :

                word = tag.split('\t')[0]
                grammatical_category = tag.split('\t')[1]
                lemma = tag.split('\t')[2]

                # si tags_list est vide ou si le mot a une categorie grammaticale eligible
                if (not tags_list) or (grammatical_category in tags_list) :

                    # on ecrit le mot dans le fichier target.csv
                    if (lemma != "<unknown>") :
                        filtered_document += lemma + " "
                    else :
                        filtered_document += word + " "
                    
        destination_file.write(filtered_document + "\n")
        destination_file.flush()    

        
    
    
    

