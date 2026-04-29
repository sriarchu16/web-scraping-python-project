
#Python Script to Read and Print Quotes from CSV
import csv

# Open the CSV file and read the data
with open('quotes.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        if row:  # Ensure the row is not empty
            print(row[0])  # Print each quote (assuming quotes are in the first column)