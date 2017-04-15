

def execute_file(filePath):

    
    with open(filePath, "r") as file:
        fileContent = file.read()
        file.close()
    exec(fileContent)
    
