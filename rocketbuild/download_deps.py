import urllib.request
import zipfile
from os import remove

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
    return