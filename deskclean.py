from watchdog.observer import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler): 
    def on_modified(self, events): 
        for filename in os.listdir(folder_to_track):
            i = 1

            if filename != 'Sorted': # this is to check if the sorted thing is already working
    
                new_name = filename
                #this is where it stops working
                extension = 'noname'

                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1]) 
                    path = extensions_folders[extension]
                except Exception:
                    extension = 'noname' #this occurs if the typical file extension is not known. 

                
                now = datetime.now() 
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders[extension] #redefine the name of object (file) as where it should be put in

                year_exists = False
                month_exists = False
                
                for folder_name in os.listdir(extensions_folders[extension]): #to sort then in defferent folders depending on time
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "/" + year
                        year_exists = True

                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists: #this creates new folders if the folders not yet exists
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month
                

                split_name = filename.split(".") #this is to ensure to not replace already existing files
                #until here
                file_exists = os.path.isfile(folder_destination + "/" + new_name)

                while file_exists: #adds a counter before the extension to not contradict
                    i += 1
                    new_name = os.path.splitext(folder_to_track + "/" + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                    #new_name = os.path.splitext(folder_to_track + "/" + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination + "/"  + new_name)

                src = folder_to_track + "/" + filename
                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)

#extension library
#if found online, can download a already fixed libreary for all
#however they are not separated based on type of files so this doesnt really work. 
extensions_folders = {
    #No Name
    'noname' : "/Users/fzdanial/Downloads/Sorted/Random",
    #Audio
    '.aif' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.cda' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.mid' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.midi' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.mp3' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.mpa' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.ogg' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.wav' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.wma' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.wpl' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    '.m3u' : "/Users/fzdanial/Downloads/Sorted/Media/Audio",
    #pictures
    '.ai': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.bmp': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.gif': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.ico': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.jpg': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.jpeg': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.png': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.ps': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.psd': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.svg': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.tif': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.tiff': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    '.CR2': "/Users/fzdanial/Downloads/Sorted/Media/Pictures",
    #video
    '.3g2': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.3gp': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.avi': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.flv': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.h264': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.m4v': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.mkv': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.mov': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.mp4': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.mpg': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.mpeg': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.rm': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.swf': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.vob': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    '.wmv': "/Users/fzdanial/Downloads/Sorted/Media/Video",
    #compressed
    '.7z': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.arj': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.deb': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.pkg': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.rar': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.rpm': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.tar.gz': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.z': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    '.zip': "/Users/fzdanial/Downloads/Sorted/MISC/Compressed",
    #exec
    '.apk': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.bat': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.com': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.exe': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.gadget': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.jar': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    '.wsf': "/Users/fzdanial/Downloads/Sorted/MISC/Executables",
    #presentations
    '.key': "/Users/fzdanial/Downloads/Sorted/Work/Presentations",
    '.odp': "/Users/fzdanial/Downloads/Sorted/Work/Presentations",
    '.pps': "/Users/fzdanial/Downloads/Sorted/Work/Presentations",
    '.ppt': "/Users/fzdanial/Downloads/Sorted/Work/Presentations",
    '.pptx': "/Users/fzdanial/Downloads/Sorted/Work/Presentations",
    #data
    '.csv': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Excel",
    '.dat': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.db': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.dbf': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.log': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.mdb': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.sav': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.sql': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.tar': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.xml': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.json': "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.txt' : "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Other",
    '.ods' : "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Excel",
    '.xlr' : "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Excel",
    '.xls' : "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Excel",
    '.xlsx' : "Users/fzdanial/Downloads/Sorted/Work/Py_Data/Excel",
    #python
    '.py' : "/Users/fzdanial/Downloads/Sorted/Work/Py_Gram",
    '.ipynb' : "/Users/fzdanial/Downloads/Sorted/Work/Py_Gram",
    #text
    '.doc' : "/Users/fzdanial/Downloads/Sorted/Work/Text/Word",
    '.docx' : "/Users/fzdanial/Downloads/Sorted/Work/Text/Word",
    '.pdf': "/Users/fzdanial/Downloads/Sorted/Work/Text/PDF",
    '.rtf': "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
    '.tex': "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
    '.wks ': "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
    '.wps': "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
    '.wpd': "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
    '.odt ' : "/Users/fzdanial/Downloads/Sorted/Work/Text/Other",
}

folder_to_track = '/Users/fzdanial/Downloads'
folder_destination = '/Users/fzdanial/Downloads/Sorted'
#sort_path = 
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join() 