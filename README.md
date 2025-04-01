# Directory Structure Viewer

A simple tool to generate and copy the folder structure of any directory. Useful for project documentation, code collaboration, and file organization.

## Features

- Select a folder and view its structure
- Copy the folder structure to the clipboard
- Simple and lightweight GUI

## Installation

~~~bash
https://github.com/granthanchatterjee/Directory-Structure-Viewer.git
cd Directory-Structure-Viewer
pip install pyperclip
~~~

## How to Use

~~~bash
python main.py
~~~

1. Click "Select Folder" to browse a directory  
2. View the folder structure in the text box  
3. Click "Copy to Clipboard" to copy the structure

## Use Cases

- **Project Documentation**: Quickly generate a folder tree for README files
- **Code Review & Collaboration**: Share project directory layout with team members
- **Organizing Files & Directories**: Visualize large folders for better management
- **Educational Purposes**: Teach best practices in file organization
- **Scripting & Automation**: Modify into a CLI tool for directory auditing

## Example
### Input
Suppose there the folder named ```Main Folder``` which has 2 folders namely ```Sub Folder 1``` and ```Sub Folder 2``` where ```Sub Folder 1``` has a file called ```Example.txt``` just like the below image<br><br>
![image](https://github.com/user-attachments/assets/b9c92805-905e-44de-b32e-0418f978617e)

### Output
~~~bash
Main Folder
├─ Sub Folder 1
│  └─ Example.txt
└─ Sub Folder 2
~~~

## Screenshots
Starting GUI which allows users to load the folder<br>
![image](https://github.com/user-attachments/assets/43529fa2-9431-4268-9a63-5487a9de49dc)
<br><br>

After selecting the folder<br>
![image](https://github.com/user-attachments/assets/0d52f79b-c291-4f80-b01f-34f314429778)
<br><br>

After clicking ```Copy to Clipboard```, the path is copied<br>
![image](https://github.com/user-attachments/assets/729e5ce2-52e9-4d8d-a3f5-f9e7d1ea7fed)

