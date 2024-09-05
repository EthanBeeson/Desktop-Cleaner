# Automatic File Organizer

## Description
The **Automatic File Organizer** is a Python script that monitors a specified directory (in this case, the "Downloads" folder) and automatically moves files to designated directories based on their file type and characteristics. It uses the `watchdog` library to observe changes in the folder and organize the files accordingly. This can help you keep your Downloads folder tidy without needing to manually organize files.

## Features
- **Automated File Sorting:** Moves files from the Downloads folder to specific directories based on file types (audio, video, images, documents, etc.).
- **File Deduplication:** If a file with the same name already exists in the target folder, the script renames the new file to avoid overwriting.
- **Real-Time Monitoring:** Uses the `watchdog` library to monitor the Downloads folder and move files as soon as they are downloaded or modified.
- **Customizable Directories:** The destination folders for different file types can be customized as needed.

### Prerequisites
- **Python 3.x** installed on your machine.
- Install the necessary Python packages:
   ```bash
   pip install watchdog

#### Modify the source destination directories in the script to match your file paths:
    source_dir = "C:\\Users\\jamie\\Downloads"
    dest_dir_music = "C:\\Users\\jamie\\Music\\Playlists"

### File Types and Destinations

#### Audio Files (.wav, .mp3)
- Small files (less than 25MB) or those containing "SFX" are moved to the sounds directory.
- Larger files are moved to the music playlists directory.

#### Moved to the videos directory.
- Video Files (.mov, .mp4)

#### Moved to the pictures/camera roll directory.
- Image Files (.jpg, .jpeg, .png)

#### Moved to the pictures/CamScanner directory.
- CamScanner Files

#### Moved to the installers directory.
- Installer Files (.exe)

#### Moved to the Word documents directory.
- Word Documents (.docx)

#### Moved to the power points directory.
- PowerPoint Files (.pptx)

#### Moved to the PDFs directory.
- PDF Files (.pdf)
  
### Technologies Used
- Python: Core programming language for implementing file operations and monitoring directories (automation)
- Watchdog: A python library used to monitor file system events (e.g., creating, modifying files)
- Shutil: Python module for moving files
- OS: Standard Python library for interacting with the file system (checking file paths, renaming, etc.)
