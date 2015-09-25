# import libraries
import xml.etree.ElementTree as ET
import json

# parse XML
parsedXmlOutput = ET.parse("KwkDict - Kwak'wala.xml")
root = parsedXmlOutput.getroot()

# list variable to house newLemma dicts
lemmaList = [];

# collect LemmaSigns and Definitions, create newLemma dicts and append them to lemmaList
for child in root:
    newLemma = {"word":[], "definition":[]}
    for child in child:
        if child.tag == "Lemma.LemmaSign":
            newLemma["word"].append(child.text)
        elif child.tag == "Sense":
            for child in child:
                if child.tag == "Definition":
                    for child in child:
                        if child.tag == "Definition.Definition":
                            newLemma["definition"].append(child.text)
    lemmaList.append(newLemma)

# create json
json = json.dumps(lemmaList)

# write to new file
textfile = open('dictionary_output.json','wb')
textfile.write(json)
textfile.close()