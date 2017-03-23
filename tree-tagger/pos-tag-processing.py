import re
import subprocess

data_set_file = open("../data/dataset.csv", "r");
pos_tag_file = open("pos_tag.csv", "a");

tags_list = ['JJ', 'JJR', 'JJS'] # liste des tags sur les mots a garder

# lecture de chaque document contenu dans dataset.csv
for data_line in data_set_file :

    # envoi de la sortie de echo dans l'entree de tree-tager-english
    echo_stdout = subprocess.Popen(('echo', data_line), stdout=subprocess.PIPE)
    tree_tagger_stdout = subprocess.run(['tree-tagger-english', ''],
                                        stdin=echo_stdout.stdout,
                                        stdout=subprocess.PIPE).stdout.decode('utf-8') 

    # lecture de chaque ligne du document tagge
    for tree_tagger_line in tree_tagger_stdout.split('\n') :

        if (len(tree_tagger_line) == 3) :
            grammatical_category = tree_tagger_line.split('\t')[1]
        
            if (grammatical_category in tags_list) :
                pos_tag_file.write(tree_tagger_line.split()[2] + " ")
        
        
    
    
    

