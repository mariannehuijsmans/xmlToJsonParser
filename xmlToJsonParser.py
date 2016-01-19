# import libraries
import xml.etree.ElementTree as ET
import json
import sys

# parse XML
parsedXmlOutput = ET.parse(sys.argv[1])
root = parsedXmlOutput.getroot()

# list variable to house newLemma dicts
lemmaList = [];

# collect LemmaSigns and Definitions, create newLemma dicts and append them to lemmaList
for entry in root:
    newLemma = {"word":[], "definition":[]}
    for word in entry.iter("Lemma.LemmaSign"):
        newLemma["word"].append(word.text)
    for definition in entry.iter("Definition.Definition"):
        newLemma["definition"].append(definition.text)
    lemmaList.append(newLemma)

# create json
json = json.dumps(lemmaList)

# write to new file
textfile = open('dictionary_output.json','wb')
textfile.write(json)
textfile.close()