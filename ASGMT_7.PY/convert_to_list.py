import csv

with open('tryout.csv') as csvfile:
    reader = csv.reader(csvfile)

    count = 0
    fsa = []

    for index,row in enumerate(reader):
        # count = count + 1
        print(row[0])
        # if count < 1000:
        #     print("breaking", count)
        #     break
        fsa.append(row)
    print("fsa", fsa)


