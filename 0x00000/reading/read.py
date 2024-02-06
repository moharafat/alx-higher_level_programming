import os
with open("mydata.txt", mode="w", encoding="utf-8")as myFile:
    myFile.write("some random txt\n more random\nsamodasd")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())
print(myFile.closed)
print(myFile.name)
print(myFile.mode)
os.rename("mydata.txt", "mydata9999.txt")
os.remove("mydata9999.txt")
#os.mkdir("mydir")
os.chdir("mydir")
print("Current Directory :", os.getcwd())
os.chdir("..")
print("Current Directory :", os.getcwd())
os.rmdir("mydir")
