import csv


filename = input("name of the file with extension .csv: ")

with open(filename, mode="r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    with open("new_ob.csv", mode="w", newline="") as ob_file:
        ob_writer = csv.writer(ob_file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            try:
                new_column = [row[7], row[10], row[11], row[17]]   # for supplier the last column = row[16]
                if row[7] == "":
                    pass
                else:
                    ob_writer.writerow(new_column)
            except:
                pass


            

