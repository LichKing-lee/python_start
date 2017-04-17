# 폴더 탐색하기
import os
import sys

dirName = sys.argv[1]


def folderTreeSearch(dirName):
    fileNames = os.listdir(dirName)
    for fileName in fileNames:
        fullName = os.path.join(dirName, fileName)
        if os.path.isdir(fullName):
            folderTreeSearch(fullName)
        else:
            print(fullName)


folderTreeSearch(dirName)
