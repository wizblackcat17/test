import csv

with open('tryout.csv') as csvfile:
    reader = csv.reader(csvfile)

    count = 0
    fsa = []

    for row in reader:
        count = count + 1
        print(row[0])
        if count < 1000:
            break
        fsa.append(row)


