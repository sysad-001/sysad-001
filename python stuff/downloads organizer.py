import os
import shutil
import mimetypes

#determine if y contains x, then move to z if true
#determine if the file type contains a certain string then move to folder if such is true
def determine(x,y,z):
    if x in mimetypes.guess_type(y)[0]:
        shutil.move(y,z)
        print ("moved", y, "to", z)
        
#for file extensions that require special treatment
#cuntbag shitfaced little stuff like webp yucky
def exception(x,y,z):
    if y.endswith(x):
        shutil.move(y,z)
        print ("moved", y, "to", z )

#establish society       
os.chdir('D:\DOWNLOAD')
downloads=os.path.dirname(os.path.realpath(__file__))
folders=['IMAGES','FOLDERS','VIDEOS','APPLICATIONS','ARCHIVES','ETC','DOCUMENTS','AUDIO']
exceptionisms=["downloads organizer.py", "vibranceGUI.exe", "youtube-dl.exe"]
#check if folders actually exist
for x in folders:
    if x in os.listdir():
        print(x, "exists, no need to create new directory")
    else:
        print(x, "does not exist, creating directory...\n")
        os.mkdir(x)

#the juice
for file in os.listdir():
    if file not in folders and file not in exceptionisms:
        try:
            # exceptions. fuck these file types (except for .rar)
            # just kidding, fuck mimetypes for not recognizing these
            # just kidding, fucking the system only applies when the system is deliberately fucking you
            # we do live in a society
            """ i do know
                that multi-line
                comments
                                exist
                                                yes


                                            this

                                    is

                        true
                        
                        """
            exception(".webp", file, 'IMAGES')
            exception(".rar",file,'ARCHIVES')
            exception(".msi",file,'APPLICATIONS')
            exception(".htm",file,'DOCUMENTS')

            #is it a directory?
            if os.path.isdir(file):
                shutil.move(file,'FOLDERS')

            #Nonetypes are nonces. 
            if mimetypes.guess_type(file)[0] !=None:
    
                
                determine('video', file, 'VIDEOS')
                determine('image', file, 'IMAGES')
                determine('document', file, 'DOCUMENTS')
                determine('pdf', file, 'DOCUMENTS')
                determine('text', file, 'DOCUMENTS')
                determine('zip', file, 'ARCHIVES')
                determine('octet', file, 'APPLICATIONS')
                determine('audio', file, 'AUDIO')
                
            #for filetypes i may or may not care about
            else:
                shutil.move(file,'ETC')
        #i genuinely just got lazy so i just said fuck it! if file not found, go eat shit and next!
        except FileNotFoundError:
            pass
        except PermissionError:
            print(file, "may be open! or you have no permission. Find it out yourself, fool")
        except shutil.Error:
            print(file, "may already exist in folder! Find out yourself, fuckface.")
