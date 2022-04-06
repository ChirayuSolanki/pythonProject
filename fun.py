import os,sys
fname = input("Enter file name : ")
if os.path.isfile(fname):
    f = open(fname,'r')
else :
    print(fname, " does not exists.")
    sys.exit()

print("The content of file is :")
str = f.read()
print(str)
f.close()