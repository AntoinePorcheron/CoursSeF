import os
import re


def CleanLine(line):
    return line.replace('\n', '')


def LoadFolders(filename):
    result = []
    with open(filename, 'r') as file:
        curr_line = file.readline()
        while curr_line != '':
            prod, test = CleanLine(curr_line).split(";")
            result.append([prod, test])
            curr_line = file.readline().lower()
    return result


def CountLine(filename):
    result = {"CLI": 0, "BAN": 0}
    with open(filename, 'r', encoding='latin-1') as file:
        line_type = file.readline()[:3]
        while line_type != '':
            if line_type in ["CLI", "BAN"]:
                result[line_type] += 1
            line_type = file.readline()[:3]
    return result


def DFS(source, pattern):
    pattern = re.compile(pattern)
    vicinity = [source]
    seen = []
    result = []
    while len(vicinity) > 0:
        source = vicinity.pop()
        if hash(source) not in seen:
            seen.append(hash(source))
            for son in map(lambda e: os.path.join(source, e), os.listdir(source)):
                if os.path.isfile(son):
                    filename = son.split("\\")[-1]
                    if pattern.match(filename):
                        result.append(os.path.join(source, son))
                else:
                    vicinity.append(os.path.join(source, son))
    return result


def ElementsToHash(elements):
    return {element: hash(element) for element in elements}


def HashToElements(elements):
    return {hash(element): element for element in elements}


def main():
    EDIT = ".*\.edit$"
    ANO = ".*\.ano$"

    prodTestFolders = LoadFolders("test.txt")

    hashList = ElementsToHash([folder for folders in prodTestFolders for folder in folders])
    hashList.update(HashToElements([folder for folders in prodTestFolders for folder in folders]))

    hashMap = {hash(prod): hash(test) for prod, test in prodTestFolders}
    hashMap.update({hash(test): hash(prod) for prod, test in prodTestFolders})

    hashProd = {hash(prod): hash(prod) for prod, test in prodTestFolders}
    hashProd.update({hash(test): hash(prod) for prod, test in prodTestFolders})

    files = []
    for folder in [f for folders in prodTestFolders for f in folders]:
        for pattern in [EDIT, ANO]:
            for file in [toLower.lower() for toLower in DFS(folder, pattern)]:
                hashList[hash(file)] = file
                hashList[file] = hash(file)
                hashMap[hash(file)] = hash(folder)
                files.append(hash(file))

    result = {}

    final = {}

    for file in files:
        parent = hashList[hashProd[hashMap[file]]]
        folder = hashList[hashMap[file]]
        filename = hashList[file].split('\\')[-1]
        quantite = CountLine(hashList[file])
        if sum([value for value in quantite.values()]) > 0:
            if parent not in result:
                result[parent] = {}
            if folder not in result[parent]:
                result[parent][folder] = {}
            result[parent][folder][filename] = quantite
            if folder != parent:
                final[parent] = {"FOLDER" : folder}
                allFile = [filename for filename in result[parent][folder].keys()]
                for currFile in result[parent][parent].keys():
                    if currFile not in allFile:
                        allFile.append(currFile)
                for currFile in allFile:
                    qParent = result[parent][parent][currFile] if currFile in result[parent][parent] else {"CLI" : 0, "BAN" : 0}
                    qChild = result[parent][folder][currFile] if currFile in result[parent][folder] else {"CLI" : 0, "BAN" : 0}
                    final[parent][currFile] = {"CLI" : qParent["CLI"] - qChild["CLI"], "BAN" : qParent["BAN"] - qChild["BAN"]}

    with open("resultat.json", 'w') as file:
        file.write(str(final))


if __name__ == "__main__":
    main()
