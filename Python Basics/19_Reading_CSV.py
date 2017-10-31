import csv

with open('.\samplefiles\example.csv') as csvfile: # 'With' is used to take care of two simultaneous process, Open() and Close()
    readcsv = csv.reader(csvfile,delimiter=',')
    
    fruit = input('Enter a fruit to get its color: ')
    for row in readcsv:
        if row[0]==fruit:
            print(row[1].upper())
