from os.path import join
import urllib.request
from rocketbuild.write_file import write_file
from rocketbuild.rewrite_arduino import rewrite_arduino
from rocketbuild.get_deps import get_deps
from rocketbuild.download_deps import download_deps
from rocketbuild.generate_arduino import generate_arduino
from rocketbuild.generate_python import generate_python
from rocketbuild.generate_dump import generate_dump # hehe.. dump
from time import time

def rocket_build(manifest, args):
    print('Executing Rocket Build v1:')
    startTime = time()
    arduinoPath = join(args.project, 'arduino')
    pythonPath = join(args.project, 'python')
    deps = set()
    fields = []

    print('---------Processing arduino files and extracting dependencies and fields---------')
    for namespace, fileDesc in manifest.items():
        req = urllib.request.urlopen(fileDesc['fileUrl'])
        inoFile = req.read().decode('utf-8')

        deps.update(get_deps(inoFile))
        (inoFile, fileFields) = rewrite_arduino(inoFile, namespace, fileDesc['defines'], args.dueMode)
        fields.extend(fileFields)
        
        write_file(inoFile, join(arduinoPath, namespace+'.ino'))
    
    print('---------Downloading dependencies---------')
    download_deps(deps, args.libFolder)
    
    print('---------Generating arduino code---------')
    (package, methods) = generate_arduino(manifest.keys(), fields)
    write_file(package, join(arduinoPath, 'package.h'))
    write_file(methods, join(arduinoPath, 'package_update.ino'))
    write_file(generate_dump(fields), join(arduinoPath, 'dump.ino'))
    
    print('---------Generating python code---------')
    write_file(generate_python(fields), join(pythonPath, 'data_package.py'))
    
    print('----------------------------------------------')
    print('Build complete in '+str(time() - startTime)+'s')
    print('----------------------------------------------')
    print()