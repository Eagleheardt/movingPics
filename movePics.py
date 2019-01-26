#!/usr/bin/python3

import os
import shutil
 
# Windows drives below:
#sourceFolder = "c:\\Users\\agueret\\Downloads\\Test\\"
sourceFolder = "p:\Stock_Illustrations\\"
destFolder =  "p:\\Stock_Archive\\Temporary_Illustrations\\"

# Linux drives below:
# sourceFolder = "/home/andreg/Downloads/source/"
# destFolder =  "/home/andreg/Downloads/destination/"

#sourceREGEX = r"^c:\\\\Users\\\\agueret\\\\Downloads\\\\Test\\\\"
#destREGEX = ""

#re.compile(sourceREGEX)
# sourceFolder = "p:\\Stock_Photography"
# destFolder =  "p:\\Stock_Archive\\Testing\\"

sourceLen = len(sourceFolder)
destLen = len(destFolder)

def mover (mainDir):
	#fullPath = os.path.realpath(fileToMove)
	#driveLetter, relPath = os.path.splitdrive(fullPath)
	#theDirPath, thefName = re.split(pic,relPath)
	for root, dirs, files in os.walk (mainDir):
		for item in files:
			if not item.startswith("iStock"):
				fullPath = os.path.join(root, item)
				pass
				#need to get path minus the source path	
				#move file to new path
		
		
		
for root, dirs, files in os.walk (sourceFolder):
		for item in files:
			if item.startswith("Thumbs"):
				continue
			if not item.startswith("iStock"):
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
				
				
				#print(partPath[:itemLen])
				
				#itemLen = len(item)
				#destPathAndFile = destPath[destLen:]
				#justDestPath = destPathAndFile[:itemLen]
				#print("justDestPath: {}                    item{}".format(justDestPath, item))
				
				
				
				############     this works, just steps too deep, IE: the pictures are in folders named after themselves
				####################################################################################################################
				#if not os.path.exists(destPath):
				#	os.makedirs(destPath)
				#print("Moving: {} To: {}".format(fullPath,destPath))
				#
				#shutil.move(fullPath, destPath)
				####################################################################################################################
				
				
				
				
				
				
				#a, b = fullPath.split(sourceFolder)
				#print("A: {} B: {} ".format(a,b))
				#a = re.split(sourceREGEX,fullPath)
				
				
				
#for pic in os.listdir(sourceFolder):
#	if (pic.startswith("TEST")):
#		fullPath = os.path.realpath(pic)
#		driveLetter, relPath = os.path.splitdrive(fullPath)
#		theDirPath = re.split(pic,fullPath)

		#dirPath, fName = os.path.split(fullPath)
		#driveLetter, relPath = os.path.splitdrive(fullPath)
		#print(pic)
#		print(driveLetter)
#		print(relPath)
		#print(splitPath)
#		print("")
#		print("fullPath: {} \nsourceFolder: {}".format(fullPath, sourceFolder))
#		print("pic: {}\ntheDirPath: {}".format(pic,theDirPath))
		#shutil.move(sourceFolder + pic,destFolder)
		#for item in driller(sourceFolder):
		#	print(item)
                               

		

#             if pic.startswith("Test"):
#                             shutil.move(pic,"P:\Stock_Archive\Testing")
#                             print("Moving: {}".format(pic))
 
#shutil.move(pic,"p:\\Stock_Archive\\Testing\\")
                                #print(os.path.split(pic))
                               
# open folder
# cycle through
# if file does NOT start with iStock move file
# continue
# SAVE THE FILE/FOLDER STRUCTURE!!!