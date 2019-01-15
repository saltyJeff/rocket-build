#!/usr/bin/env python3
import argparse
from rocketbuild.sketchbook_dir import sketchbook_dir
from rocketbuild.rocket_build import rocket_build
import json
from os.path import join

def main():
    parser = argparse.ArgumentParser(description='Rocket build system')
    parser.add_argument('project', type=str,
                        help='Folder containing rocket manifest')
    parser.add_argument('--libFolder', help='location of Arduino sketchbook liraries')
    parser.add_argument('--dueMode', help='use double wide integer mode')

    args = parser.parse_args()
    if args.libFolder == None:
        args.libFolder = sketchbook_dir()

    with open(join(args.project, 'rocket_manifest.json')) as f:
        data = json.load(f)

    rocket_build(data, args)

if __name__ == '__main__':
    main()