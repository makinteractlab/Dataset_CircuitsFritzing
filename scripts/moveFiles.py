# moveFiles
# move files from a directory to another
# Author: Andrea Bianchi, 2019


# Usage
# python moveFiles.py -d srcDir -o ourDir


import argparse, sys, os, os.path, re, zipfile, shutil

           
def main():
    import argparse 

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--output', help='Output folder', required=True)
    parser.add_argument('-d', '--dir', help='Input root directory', required=True)

    args = parser.parse_args()

    # # output dir
    outDir= args.output
    if not os.path.exists(outDir):
        os.mkdir(outDir)


    # Get the list of all files in directory tree at given path
    dirName= args.dir
    id = 0
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        for file in filenames:
            if not (file.endswith('.fzz') or file.endswith('.fz')):
                continue

            newName= file
            newName= newName.replace(" ", "_")
            newName= newName.replace("-", "_")
            newName = "id"+str(id)+"_"+newName
            id+= 1
            shutil.copy (os.path.join (dirpath, file), os.path.join (outDir, newName))
            print newName



    

if __name__ == "__main__":
    main()



