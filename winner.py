# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Tom Sundström (office@tomsun.ax)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""
winner.py

Picks a winner from a set of candidates in a text file (one candidate per line).
This file's existence is 2% out of convenience and 98% as an inside joke.
"""

import sys
import random
import time
import codecs
import json

lang_strs = {}
def t(string):
    if string in lang_strs:
        return lang_strs[string].encode("utf-8")
    return string

def pick_winner(file):
    with codecs.open(file, "r", "utf-8") as f:
        candidates = f.readlines()

    candidates = [c.encode("utf-8") for c in candidates]

    try:
        while True:
            print candidates[random.randrange(0, len(candidates))].strip()
    except KeyboardInterrupt:
        while len(candidates) > 2:
            loser = random.randrange(0, len(candidates))
            print t("Did not win: %s") % candidates[loser].strip()
            del candidates[loser]
            print t("Remaining: %d") % len(candidates)
            time.sleep(0.2)

        print
        print t("Final round:")
        print candidates[0].strip()
        print t("VS")
        print candidates[1].strip()

        time.sleep(3)
        del candidates[random.randrange(0,2)]
        print
        print t("The winner is:")
        time.sleep(3)
        print candidates[0].strip()
        print

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='f')
    parser.add_argument('-l', '--lang')
    args = parser.parse_args()
    if args.lang:
        lang_strs = json.loads(codecs.open("%s.json" % args.lang, "r", "utf-8").read())

    pick_winner(args.file)
