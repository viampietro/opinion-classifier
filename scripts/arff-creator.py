import re

#
# PRE-REQUIS : Se placer dans le dossier contenant les fichiers data et labels
# ou specifier le chemin complet de ces fichiers. Les fichiers data et labels
# doivent avoir l'extension .csv
#
# PARAM :
# @data_file, le chemin du fichier contenant les donnees brutes,
# separees par un retour a la ligne.
# @labels_file, le chemin du fichier contenant les labels associees aux donnees brutes.
# @target_arff_file, le fichier de reception, au format arff, pour la combinaison des donnees brutes et des labels.
#
# ACTION : Associe symetriquement chaque ligne du fichier data_file avec une ligne
# du fichier labels_file et ecrit la combinaison des deux lignes dans le fichier target_arff_file
#
def csv_to_arff (data_file, labels_file, target_arff_file) :
    
    data = open(data_file + ".csv", "r", encoding="utf-8");
    labels = open(labels_file + ".csv", "r", encoding="utf-8");

    arff_file = open(target_arff_file + ".arff", "a", encoding="utf-8");


    for data_line in data :
    
        labels_line = labels.readline();
        arff_file_line = "\"" + data_line.replace("\"", "\\\"").replace("\n", "") + "\", " + labels_line;

        arff_file.write(arff_file_line);

#
# ACTION : Associe chaque ligne de data_file avec le chosen_label (string)
# et ecrit le resultat dans target_arff_file.
#
def unlabelled_csv_to_arff (data_file, chosen_label, target_arff_file) :

    data = open(data_file + ".csv", "r", encoding="utf-8");
    arff_file = open(target_arff_file + ".arff", "a", encoding="utf-8");

    for data_line in data :
    
        arff_file_line = "\"" + data_line.replace("\"", "\\\"").replace("\n", "") + "\", " + chosen_label + "\n";

        arff_file.write(arff_file_line);

#
# ACTION : ecrit toutes les lignes du fichier source_arff_file a
# la suite du fichier target_arff_file.
#
def arff_file_union (source_arff_file, target_arff_file, header_on_source=False) :

    begin_writing = False
    target = open(target_arff_file + ".arff", "a", encoding="utf-8");
    source = open(source_arff_file + ".arff", "r", encoding="utf-8");

    # si la source possede une entete arff
    if header_on_source :

        for source_line in source :
            
            if begin_writing :

                target.write(source_line)

            elif source_line == "@data\n" :

                print("@data atteint")
                begin_writing = True
                
    # si l'entete arff n'est pas placee
    else :
        
        for source_line in source :

            target.write(source_line)
