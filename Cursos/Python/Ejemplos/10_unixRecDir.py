from subprocess import getoutput
from os import getcwd, chdir

def getLines():
    directory = getoutput("ls -l")
    return directory.splitlines()

def getFiles():
    lines = getLines()
    dirs = [getcwd()+"/" + d.split()[-1] \
        for d in lines[1:] if d.split()[0][0] == "d"]
    files = [d.split()[-1] for d in lines[1:]\
            if d.split()[0][0] == "-"]
    allFiles = [x.split()[-1] for x in lines[1:]]
    return dirs, files, allFiles

dirs,files,allFiles = getFiles()

#print "All: "
#print allFiles
#print "\n\nFiles:"
#print files
print("INICIO", getcwd(), "con los directorios:")
print("Dirs:", [x.split("/")[-1] for x in dirs], "\n")

while(len(dirs)>0):
    path = getcwd()
    next_dir = dirs.pop(0)
    chdir(next_dir)

    dirs2,files2,allFiles2 = getFiles()
    print("Dirs(%s):" % next_dir.split("/")[-1], [x.split("/")[-1] for x in dirs2], "\n")
    dirs = dirs2 + dirs
