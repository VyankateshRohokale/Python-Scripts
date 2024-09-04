import sys
import os
import shutil


def deletefile(path):
    
    files = os.listdir(path)

    for file in files:
        if os.path.isfile(os.path.join(path,file)):
            os.remove(os.path.join(path,file))


def createfolder(path):

    path2 = path
    fol = "videos"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    path = path2

    fol = "audios"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    path = path2

    fol = "pictures"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    path = path2

    fol = "other"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    path = path2

    fol = "text"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    
    path = path2

    fol = "mp4"
    path = os.path.join(path,fol)
    if not os.path.isdir(path):
        os.mkdir(path)

    path = path2


def filesort(path):

    try:
        fname = ""
        for k,j,i in os.walk(path):

            for file in i:

                if file.endswith(".txt"):
                    fromthis = os.path.join(path, file)
                    tothis = os.path.join(path, "text")
                    shutil.move(fromthis,tothis)
            
                elif file.endswith(".avi") or file.endswith(".mov"):
                    fromthis = os.path.join(path, file)
                    tothis = os.path.join(path, "videos")
                    shutil.copy(fromthis,tothis)

                elif file.endswith(".jpg") or file.endswith(".jpeg"):
                    fromthis = os.path.join(path,file)
                    tothis = os.path.join(path,"pictures")
                    shutil.copy(fromthis,tothis)
                
                elif file.endswith(".mp3") or file.endswith(".m4a"):
                    fromthis = os.path.join(path,file)
                    tothis = os.path.join(path,"audios")
                    shutil.copy(fromthis,tothis)
            
                elif file.endswith(".mp4"):
                    fromthis = os.path.join(path,file)
                    tothis = os.path.join(path,"mp4")
                    shutil.copy(fromthis,tothis)

                else:
                    fromthis = os.path.join(path,file)
                    tothis = os.path.join(path,"other")
                    shutil.copy(fromthis,tothis)


    except Exception as E:
        
        print("This File Already Exists -> ",file )




def main():



    print("-------------------------------------------------------------------------------------------------------")
    print("Welcome To Automated Sorting Script By Piyush Rohokale...")

    if len(sys.argv) != 2:
        print("Please Enter the Path as CommandLine Argument To the Script....")
        print("-------------------------------------------------------------------------------------------------------")
        exit()

    if not os.path.isabs(sys.argv[1]):

        sys.argv[1] = os.path.abspath(sys.argv[1])




    print("Your Entered Path is : ",sys.argv[1])

   
    print("Creating Folders...")
    path = sys.argv[1]

    createfolder(path)

    print("Folders Are Created...")

    print("Sorting The Files To There Designeted Folders...")

    filesort(path)

    deletefile(path)

    


                
    print("Files Have been sorted...")


    print("-------------------------------------------------------------------------------------------------------")
    print("     Leetcode     -> https://leetcode.com/u/piyushrohokale2525/")
    print("      Github      -> https://github.com/VyankateshRohokale")
    print("  Email Address   -> piyushrohokale2525@gmail.com")

    print("-------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
