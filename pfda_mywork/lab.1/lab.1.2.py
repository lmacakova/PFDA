import csv
FILENAME= "data.csv"
DATADIR = "where did you put it"
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:         
        print (line) 




















