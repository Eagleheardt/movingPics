#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog

import os
import shutil

sourcePath = StringVar() # Path of source folder
destinationPath = StringVar() # Path of destination folder
sourceInfo = StringVar() # Display of source folder
destinationInfo = StringVar() # Display of destination folder

sourcePathLen = IntVar()
destinationPathLen = IntVar()

sourceFolder = "p:\Stock_Illustrations\\"
destFolder =  "p:\\Stock_Archive\\Temporary_Illustrations\\"

sourceLen = len(sourceFolder)
destLen = len(destFolder)

sourceInfo.set("No Source Selected")
destinationInfo.set("No Destination Selected")

windowMenu=Tk() # gui window is called windowMenu
		
for root, dirs, files in os.walk (sourceFolder):
		for item in files:
			if item.startswith(startOfFile):
				fullPath = os.path.join(root, item) # full location of original file
				partPath = fullPath[sourceLen:] # path without source
				destPath = destFolder + partPath # full path, with file name, to destination
				itemLen = len(item)
				fullDestPathLen = len(destPath)
				onlyPathLen = fullDestPathLen - itemLen
				justDestPath = destPath[:onlyPathLen]
				
				if os.path.exists(justDestPath):
					os.makedirs(justDestPath) 
				print("Moving: {} To: {}".format(fullPath,destPath))
				
				shutil.move(fullPath, destPath)














windowMenu.mainloop() # this starts the GUI