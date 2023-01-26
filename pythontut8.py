import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some  more")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

# os.rename("mydata.txt", "mydata2.txt")

# os.remove("mydata2.txt")

os.mkdir("mydir")

os.chdir("mydir")

print("current working directory: ", os.getcwd())

os.chdir("..")

print("Current working directory :", os.getcwd())

os.rmdir("mydir")

with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum, " : ", line, end="")

        lineNum += 1