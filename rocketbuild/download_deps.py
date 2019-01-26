import urllib.request
import zipfile
from os import remove, rename, listdir, path
import re

INVALID = re.compile(r'-.*', re.MULTILINE)
def download_deps(deps, libFolder):
    for zipUrl in deps:
        print('downloading from '+zipUrl)
        urllib.request.urlretrieve(zipUrl, 'temp.zip')
        zipFile = zipfile.ZipFile('temp.zip')
        zipFile.extractall(libFolder)
        zipFile.close()

    try:
        remove('temp.zip')
    except:
        print('no dependencies to download')

    for folder in listdir(libFolder):
        folderPath = path.join(libFolder, folder)
        if path.isdir(folderPath):
            newName = re.sub(INVALID, '', folder)
            try:
                rename(folderPath, path.join(libFolder, newName))
            except:
                print('duplicate found, deleting old one')
                remove(path.join(libFolder, newName))
                rename(folderPath, path.join(libFolder, newName))
            print('renamed '+folder+' to '+newName)
    return