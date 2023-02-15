import os
import json

def generateFilePath(data):
    data = data["data"]
    data_id = data["id"]
    data_id_parts = data_id.split("-")
    docket_id = "-".join(data_id_parts[0:3])
    return f"./NewData/data/{data['type']}/{data['attributes']['agencyId']}/{docket_id}/" 


def makeDirectory(filepath):
    try:
        os.makedirs(filepath)
    except FileExistsError:
        print("Filepath already exits")

def main():
    for root, dirs, files in os.walk("./originalData/data/data"):
        for name in files:
            print(os.path.join(root, name))
            with open(os.path.join(root, name)) as infile:
                data = json.load(infile)
                filepath = generateFilePath(data)
                makeDirectory(filepath)
                with open(f'{filepath}{name}', 'w+', encoding='utf8') as file:
                    file.write(json.dumps(data))

main()