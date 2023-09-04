#!/usr/bin/env python3

# puz-meta.py
#
# A bit of cobbled-together python to read a .puz file, replace one of the bits of metadata
# and then write it back out TO THE SAME LOCATION
# 
# I wrote this specifically because the Forkyz app on Android, when importing, uses the author
# name as the source. Since there isn't another good data field to use for that, it makes sense.
# However, the LA Times crosswords have the puzzle author and the editor in the field, which
# leads to hundreds of different entries when sorted by source. This doesn't happen when you
# use the in-app downloader, but it does happen if you load a bunch of .puz files on the phone,
# as I typically do.
#
# At the moment, I just parse for the author field, but it might help someone in the future that
# wants to fix up some other errant field, so I'm going to document this here.
#
# Requires puzpy by alexdej
#
# Future ideas
# - Fix up input source so that it expands wildcards

import argparse
import inspect
import sys
import textwrap
import time
import os
import puz

def main():
    parser = argparse.ArgumentParser(prog='puz-meta',
                                     description=textwrap.dedent("""\
        puz-meta is a tool to replace certain values of a .puz file
        """),
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('source', help=textwrap.dedent("""\
                                File to update"""), nargs='+')

    parser.add_argument('-a', '--author',
                        help=textwrap.dedent("""\
                            Replace the author credits metadata with the following string"""),
                        default=None)

    args = parser.parse_args()

    if (args is None):
        return
    
    if (args.source is None):
        print("input file(s) required")
        return
    
    for filename in args.source:
        p = puz.read(filename)
        if (p is None):
            return
        if (args.author is not None):
            p.author = args.author
        p.save(filename)
    
if __name__ == '__main__':
    main()
