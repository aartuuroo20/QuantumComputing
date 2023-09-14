import json

archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(archivo, "r") as jsonFile:
    data = json.load(jsonFile)

print(data[1])
