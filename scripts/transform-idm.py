# Alexandre Culty (21508308)
# Maryam Soheili Majd (21613073) 
# Nicolas Delalande (20121972)
# Vincent Iampietro (20142295)

import re, os

# transform(r"path", max, nom) !
def transform (path, max, nom) :

	csv_file = open(nom + ".csv", "w", encoding="utf-8");

	i = 0;
	for filename in os.listdir(path):
		content = open(path + '/' + filename, "r", encoding="utf-8");
		csv_file.write(content.read() + "\n");
		i += 1;
		if(i >= max):
			return 0;
		
