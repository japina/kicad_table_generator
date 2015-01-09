import os

# very simple fp_lib_table generator for python
# on Mac OSX you need to copy the file to ~/Library/Preferences/kicad
# start the with: python tablegen.py  > fp-lib-table

#the idea from tablegen.sh by Sean Pepin but I had troubles in hacking the file, so ... here is the Python version for it :)


dirname = '/Users/bostjan/peskovnik/kicad/library/pcb/' # directory of the *.mod or *.pretty files/directories
dirlist = os.listdir(dirname)


print "(fp_lib_table"
for i in dirlist:
    if i.split('.')[-1]=='mod':
        print "  (lib (name " + i.replace('.mod','') +")(type Legacy)(uri " + dirname + i + ")(options \"\")(descr \"\"))"

for i in dirlist:
    if i.split('.')[-1]=='pretty':
        print "  (lib (name " + i.replace('.pretty','') +")(type KiCad)(uri " + dirname + i + ")(options \"\")(descr \"\"))"

print ")"