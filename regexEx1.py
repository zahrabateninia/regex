#!/usr/bin/env python3
import re
log = "July 31 mycomputer bad_process[12345]: ERROR performing package upgrade"
regex = r"\[(\d+)\]" # \ is scape character,() is capturing group and \d+ means match one or more numerical characters.
result = re.search(regex, log)
print(result[1])