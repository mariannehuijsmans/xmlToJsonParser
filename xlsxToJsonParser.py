# Import Libraries
from openpyxl import load_workbook 
from openpyxl.styles import Font
import sys
import json

# Load argv[1] as workbook
wb = load_workbook(sys.argv[1])
ws = wb.active

# Create wordlist
wordList = []

# Loop through rows in worksheet, create if statements for different columns and append Lemmas to wordList.
for row in ws.iter_rows('A2:C3'):
    newLemma = {"word":[], "definition":[]}
    for col in row:
        if col.column == 'A':
            print(col.value)
            newLemma["word"].append(col.value)
        if col.column == 'B':
            newLemma["definition"].append(col.value)
    wordList.append(newLemma)

# create json
json = json.dumps(wordList)

# write to new file
textfile = open('wordlist.txt','wb')
textfile.write(json)
textfile.close()

