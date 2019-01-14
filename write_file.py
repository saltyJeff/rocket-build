def write_file(s, path):
    outputFile = open(path, 'w')
    outputFile.write(s)
    outputFile.close()