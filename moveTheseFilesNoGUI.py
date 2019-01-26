#!/usr/bin/python3

import os
import shutil

sourceFolder = "p:\Stock_Illustrations\\"
destFolder =  "p:\\Stock_Archive\\Illustrations\\"
startOfFile = "Start of the file"

sourceLen = len(sourceFolder)
destLen = len(destFolder)

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
				
				if not os.path.exists(justDestPath):
					os.makedirs(justDestPath)
				print("Moving: {} To: {}".format(fullPath,destPath))
				
				shutil.move(fullPath, destPath)