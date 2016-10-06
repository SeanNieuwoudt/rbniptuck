#!/usr/bin/env python
# encoding: utf-8

'''
    A really simple way to convert old-style Ruby hashes to Ruby 1.8^ compliant syntax
    and also (while we're at it) convert uninterpolated double quoted strings into 
    single quoted strings.

    @author Sean Nieuwoudt
    @email  sean@wixelhq.com
    @date   06/08/2016
'''

import os
import re
import argparse

## Convert old-style hashes

def process_hashes(s):
    regex = re.compile(r":([a-zA-Z0-9_]+)\s*=>\s*", re.MULTILINE)
    return regex.sub(r"\1: ", s)

## Convert double quoted strings to single quoted

def process_quoted(s):
    return re.sub(r"\"([a-zA-Z0-9_-]+)\"", r"'\1'", s)

## Write the file output

def write_file(path, contents):
    file = open(path, "w")
    file.write(contents)
    print(contents)
    file.close()

## Get file contents

def get_contents(path):
    file = open(f, 'r')
    contents = file.read()
    file.close()
    return contents

## Recursively scan a directory for all matching files

def scan_dir(p, ext=".rb"):
    files = []

    for f in os.listdir(p):
        if os.path.isdir(f) == True:
            files = files + scan_dir(f)
        else:
            if f.endswith(ext):
                files.append("{0}/{1}".format(p, f))

    return files

if __name__ == "__main__":
    parser = argparse.ArgumentParser("asdasd")
    parser.add_argument('-d', '--dir', default=".")
    parser.add_argument('-e', '--ext', default=".rb")

    args = parser.parse_args()

    for f in scan_dir(args.dir, args.ext):
        contents = get_contents(f)
        contents = process_hashes(contents)
        contents = process_quoted(contents)

        write_file(f, contents)

        print("Completed: {0} ({1} bytes)".format(f, len(contents)))
