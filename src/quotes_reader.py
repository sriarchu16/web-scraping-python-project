
import os
import csv

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "quotes.csv")

with open(file_path, mode="r", encoding="utf-8", errors="replace") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)