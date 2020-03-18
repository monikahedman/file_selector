# Sequential File Selector 

## Description
This file selector allows the user to browse through their file system and either display iterative files in both expanded and collapsed ways. Sequential files are displayed in the following format: [baseName].%[framePadding].[extension] [startFrame]-[endFrame].

For example:
- taco.0001.jpg
- taco.0002.jpg
- taco.0003.jpg
	
Collapses to:
- taco.%04d.jpg 1-3

But, this does not collapse:
- comp_v001.mb
- comp_v002.mb

## Installation
Download from GitHub: https://github.com/monikahedman/file_selector

## Dependencies
Required to run the file selector:
- Pyside2
- Python 2.7
- QT Version 5.14.1

## Running
Navigate to the project directory and run the main file:
```bash
python main.py
```

## Usage
All of the files displayed in the "File System" section are collapsed. For file navigation, the user can:
- Type in a file path in the File Path text box. Press "Go" or the enter key to navigate to that folder.
- Click on a single folder on the lefthand side (indicated by the third column) and press the ">" key at the top right of that box to navigate into that folder
- Alternatively, press the "<" key in the same section to navigate to the parent folder

All files selected on the lefthand side will appear on the right. When on the right, they can be either expanded or collapsed. Click the "Expand Collapsed/Collapse Files" button to toggle between collapsed and uncollapsed. If the user double clicks on any of the files on the righthand side, they will be opened in the operating system's default application for that file type.

Other notes: The user can select all or deselect all files in the File System with the buttons on the bottom. Multi-select can either be enabled or disabled, but it is enabled by default.
