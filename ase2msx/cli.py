# -*- coding: utf-8-unix -*-

# Copyright (c) 2025 Daishi Mori (mori0091)
#
# This software is released under the MIT License.
# See https://github.com/mori0091/ase2msx

VERSION = '1.0.1'

def main():
    import argparse
    import os
    import shutil
    from subprocess import call
    import sys
    from . import sheet

    parser = argparse.ArgumentParser(
        prog='ase2msx',
        description='Generates sprite data and code for libmsx/MSX2 from Aseprite file.'
    )
    parser.add_argument('filenames',
                        help='input aseprite file(s)',
                        nargs='+')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+VERSION,
                        help='show version and exit')
    args = parser.parse_args()

    ASEPRITE = shutil.which('aseprite')
    if ASEPRITE == None:
        ASEPRITE = shutil.which('aseprite.exe')
        if ASEPRITE == None:
            print(f'aseprite not found.')
            sys.exit(1)

    ASEFLAGS = ['--format json-hash',
                '--sheet-pack',
                '--ignore-empty',
                '--merge-duplicates',
                '--list-tags']

    for a_ase in args.filenames:
        folder, filename = os.path.split(a_ase)
        name, ext = os.path.splitext(filename)
        if not os.path.exists(a_ase):
            print(f"File not found - '{a_ase}' skipped.")
        elif not os.path.isfile(a_ase):
            print(f"Not a regular file - '{a_ase}' skipped.")
        elif ext != '.ase' and ext != '.aseprite':
            print(f"Not an aseprite file - '{a_ase}' skipped.")
        else:
            a_json = name + '.json'
            a_png = name + '.png'
            cmdline = ' '.join([ASEPRITE, f'--batch --data {a_json} --sheet {a_png}', *ASEFLAGS, a_ase])
            try:
                retcode = call(cmdline, shell=True)
                if retcode < 0:
                    print(f"{ASEPRITE} was terminated by signal", -retcode, file=sys.stderr)
                    sys.exit(retcode)
                elif retcode != 0:
                    print(f"{ASEPRITE} returned", retcode, file=sys.stderr)
                    sys.exit(retcode)
            except OSError as e:
                print(f"Execution failed - {ASEPRITE}:", e, file=sys.stderr)
                sys.exit(1)

            sheet.convert(filename, a_json, a_png)
