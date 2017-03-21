import re


data_set_file = open("dataset.csv", "r");
labels_file = open("labels.csv", "r");

arff_file = open("opinion.arff", "a");



for data_set_file_line in data_set_file :
    
    labels_file_line = labels_file.readline();
    arff_file_line = "\"" + data_set_file_line.replace("\"", "\\\"").replace("\n", "") + "\", " + labels_file_line;

    arff_file.write(arff_file_line);

    
    
    



