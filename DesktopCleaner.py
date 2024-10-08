import os
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folders to Organize Downloads into
source_dir = "C:\\Users\\jamie\\Downloads"
dest_dir_sfx = "C:\\Users\\jamie\\Music\\sounds"
dest_dir_music = "C:\\Users\\jamie\\Music\\Playlists"
dest_dir_video = "C:\\Users\\jamie\\Videos"
dest_dir_image = "C:\\Users\\jamie\\Pictures\\Camera Roll"
dest_dir_camScanner = "C:\\Users\\jamie\\Pictures\\CamScanner"
dest_dir_installer = "C:\\Users\\jamie\\Documents\\Installers"
dest_dir_wordDocuments = "C:\\Users\\jamie\\Documents\\Word Documents"
dest_dir_PDF = "C:\\Users\\jamie\\Documents\\PDFs"
dest_dir_powerPoints = "C:\\Users\\jamie\\Documents\\Power Points"

def makeUnique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    # if file exists, adds number to the end of the filename
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if os.path.exists(os.path.join(dest, name)):
        unique_name = makeUnique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        os.rename(oldName, newName)
    move(entry, dest)
    
class MoverHandler(FileSystemEventHandler):
    # Function runs whenever a change is made to the downloads file aka "source_dir"
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move_file(dest, entry, name)
                    logging.info(f"Moved audio file: {name}")
                elif name.endswith('.mov') or name.endswith('.mp4'):
                    dest = dest_dir_video
                    move_file(dest, entry, name)
                    logging.info(f"Moved video file: {name}")
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
                    dest = dest_dir_image
                    move_file(dest, entry, name)
                    logging.info(f"Moved image file: {name}")
                elif name.endswith('.exe'):
                    dest = dest_dir_installer
                    move_file(dest, entry, name)
                    logging.info(f"Moved .exe installer file: {name}")
                elif "CamScanner" in name:
                    dest = dest_dir_camScanner
                    move_file(dest, entry, name)
                    logging.info(f"Moved CamScanner file: {name}")
                elif name.endswith('.pptx'):
                    dest = dest_dir_powerPoints
                    move_file(dest, entry, name)
                    logging.info(f"Moved power point file: {name}")
                elif name.endswith('.docx'):
                    dest = dest_dir_wordDocuments
                    move_file(dest, entry, name)
                    logging.info(f"Moved word document: {name}")
                elif name.endswith('.pdf'):
                    dest = dest_dir_PDF
                    move_file(dest, entry, name)
                    logging.info(f"Moved PDF file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

