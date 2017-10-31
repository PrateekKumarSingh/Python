import csv
# put a try block whereever you think an error could occur
try:
    with open('.\\samplefiles\\NoSuchFile.csv') as csvfile: 
        readcsv = csv.reader(csvfile,delimiter=',')
        
        fruit = input('Enter a fruit to get its color: ')
        for row in readcsv:
            if row[0]==fruit:
                print(row[1].upper())
except Exception as e: # If an exception is catched in the try block, the except block is executed
    print(e)

print('continuing')   # if no exception is catched the program continues