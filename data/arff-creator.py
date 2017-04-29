import re

def csv_to_arff (csv_file_name) :
    
    data_set_file = open(csv_file_name + ".csv", "r", encoding="utf-8");
    labels_file = open("labels.csv", "r", encoding="utf-8");

    arff_file = open(csv_file_name + ".arff", "a", encoding="utf-8");



    for data_set_file_line in data_set_file :
    
        labels_file_line = labels_file.readline();
        arff_file_line = "\"" + data_set_file_line.replace("\"", "\\\"").replace("\n", "") + "\", " + labels_file_line;

        arff_file.write(arff_file_line);

