#!/usr/bin/python3

file_source = open('main.py', 'r')
file_dest = open('foyerApp.py', 'w')

line = 1
for textLine in file_source:
    if line == 1:
        file_dest.write("#!/opt/FoyerSociety/env/bin/python3")
    else:
        file_dest.write(textLine)
        
    line += 1