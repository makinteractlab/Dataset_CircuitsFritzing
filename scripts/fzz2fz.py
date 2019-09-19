# fzz2fz
# convert one or multiple Fritzing files from fzz to fz format
# Author: Andrea Bianchi, 2019


# Usage
# python fzz2fz.py -f file[s] -o outputDir


import argparse, sys, os, os.path, re, zipfile, shutil
    

def moveAllFz (newBaseName, fromDir, toDir):
    # move fz to output
    id= 0
    for root, dirs, files in os.walk(fromDir, topdown=False):
        for fz in files:
            if not fz.endswith('.fz'):
                continue

            fileName = newBaseName + "_"+ str(id) + ".fz"
            id+= 1
            shutil.move (os.path.join (fromDir, fz), os.path.join (toDir, fileName))

           
def main():
    import argparse 

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--output', help='Output folder', required=True)
    parser.add_argument('-f', '--files', help='Input files', nargs='+', required=True)

    args = parser.parse_args()

    # output dir
    outDir= args.output
    if not os.path.exists(outDir):
        os.mkdir(outDir)


    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED

    # rename fzz and extract to tempDir
    for fzz in args.files:
        if not fzz.endswith('.fzz'):
            continue

        # temp dir
        tempDir= "___temp___"
        if not os.path.exists(tempDir):
            os.mkdir(tempDir)

        fzzName= os.path.basename(fzz)
        tempFzz= os.path.join (tempDir, fzzName)
        shutil.copyfile(fzz, tempFzz)
         
        name= tempFzz[:-4]
        zipName= name+".zip"
        os.rename(tempFzz, zipName)

        extractedName= fzzName[:-4]
        print extractedName
        zf = zipfile.ZipFile(zipName)
        zf.extractall(tempDir)
        zf.close()

        moveAllFz (extractedName, tempDir, outDir)

        # delete tempDir
        try:
            shutil.rmtree(tempDir)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

    


    

if __name__ == "__main__":
    main()



