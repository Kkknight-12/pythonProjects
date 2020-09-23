import os

directory = r'/Users/knight/Documents'


def getfiles():
    # enmpty list to store the pdfFile names
    name = []
    """
    loop will iter over all the files and store 
    the name of file which ends with pdf
    """
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            name.append(filename)
        else:
            continue
    return name


print(getfiles())
