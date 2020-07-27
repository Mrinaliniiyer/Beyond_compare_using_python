import subprocess
import os
import re
import sys
path1=sys.argv[1]
path2=sys.argv[2]
path3=sys.argv[3]
#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
folder1=[]
folder2=[]
for r, d, f in os.walk(path1):
    for folder in f:
        folder1.append([folder,os.path.join(r,folder)])
for r, d, f in os.walk(path2):
    for folder in f:
        folder2.append([folder,os.path.join(r,folder)])
for i in range(0,len(folder1)):
    #print(folder1[i])
    for j in range(0,len(folder2)):
        #print(folder2[j])
        c=j[:2]
        print(c)
        if folder1[i][0]==folder2[j][0]:
            newfolder=folder1[i][0].split(".")
            newfolder[1]='html'
            s='.'
            abc=s.join(newfolder)
            f = open(os.path.join(path3,abc),'wb')
            f.close()
            #subprocess.Popen('C:\Program Files (x86)\Beyond Compare 3\BCompare.exe '+folder1[i][1]+' '+folder2[j][1]+' savetarget="C:\\Users\\admin\\Documents\\project\\compared\\"'+abc)
            subprocess.Popen('C:\Program Files (x86)\Beyond Compare 3\BCompare.exe "@C:\\Users\\admin\\Documents\\scriptrun.txt" "'+folder1[i][1]+'" "'+folder2[j][1]+'" "C:\\Users\\admin\\Documents\\project\\compared\\"'+abc)