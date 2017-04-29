import re, os

# transform(r"path", max, nom) !
def transform (path, max, nom) :

	arff_file = open(nom + ".csv", "w", encoding="utf-8");

	i = 0;
	for filename in os.listdir(path):
		content = open(path + '/' + filename, "r", encoding="utf-8");
		arff_file.write(content.read() + "\n");
		i += 1;
		if(i >= max):
			return 0;
		