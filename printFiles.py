#!/usr/bin/python3

import os

sourceFolder = "p:\Stock_Illustrations\\"

for root, dirs, files in os.walk (sourceFolder):
		for item in files:
			fullPath = os.path.join(root, item) # full location of original file
			