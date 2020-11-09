#Samuel Parker


from PIL import Image
import tkinter as tk

#draws picture
ASCII = open("ASCII.txt", "r")
print(ASCII.read(), "\nSamuel Parker\n\n")


#Creates a text file containing ASCII representation of inputted picture.
def create():
    #takes name of file in and out, opens file in.
    nameIn = input("in>")+input("filetype>")
    name = input("out>")+".txt"
    file = open(name, "w+")

    #opens and writes contents of ASCIIartchars to a list.
    colourFile = open("ASCIIartchars.txt", "r")
    colour = list(colourFile.read())

    #opens inputted image, finds dimensions and converts to greyscale. Coverts image contents to a list.
    image = Image.open(nameIn)
    width, height = image.size
    gsimg = image.convert("L")
    arr = list(gsimg.getdata())

    #user tells how many lines are to be sampled. Highest and lowest colour values found.
    mode = int(input("mode>"))
    high = 0
    low = 300
    for i in range(len(arr)):
        if arr[i] < low:
            low = arr[i]
        if arr[i] > high:
            high = arr[i]
    colRange = high - low

    #Colour values balanced, converted to ASCII, saved to file and printed.
    for i in range(len(list(gsimg.getdata()))):
        arr[i] = ((arr[i] - low)/colRange)*256
        arr[i] = colour[int(arr[i])//4]
    for i in range(height)[::mode]:
        j = i*width
        print("\033[1m"+"".join(arr[j:j+width-1]))
        file.write("".join(arr[j:j+width-1])+"\n")

#Views a text file
def view():
    name = input("show>")+input("filetype>")
    file = open(name, "r")
    print(file.read())

#Turns a text file into a TKinter window
def tkint():
    #gets input file name and type, then splits into a list.
    fileIn = input("in>")+input("filetype>")
    fileIn = open(fileIn, "r")
    coList = (fileIn.read()).split("\n")

    #finds height and width of input data
    height = 0
    width = 0
    for i in coList:
        height += 1
    for i in range(len(coList[0])):
        width += 1

    #puts colours to different ASCII characters in a dictionary based on user input.
    colourDict = {}
    colourFile = open("ASCIIartchars.txt", "r")
    arrASCII = colourFile.read()
    arrASCII = list(arrASCII)
    colours = open("Colours.txt", "r")
    arrColours = colours.read()
    arrColours = arrColours.split(":")
    colourGap = int(input("colourGap>"))
    colourStart = int(input("colourStart>"))
    for i in range(0,64):
        d = {arrASCII[i]:arrColours[(colourStart+(i*colourGap))%len(arrASCII)]}
        colourDict.update(d)

    #makes a TKinter window and draws individual "pixels". Could be really optimised.
    top = tk.Tk()
    can = tk.Canvas(top, bg="white", height=width, width=height)
    for i in range(height-1):
        for j in range(width-1):
            line = can.create_line(i, j, i+1, j+1, fill=colourDict.get(coList[i][j]))
    can.pack()
    top.mainloop()

#runs program until user says to exit
while True:
    print("""
1:Create
2:View
3:Tkinter
4:End""")
    choicex = int(input(">"))

    if choicex == 1:
        create()
    elif choicex == 2:
        view()
    elif choicex == 3:
        tkint()
    elif choicex == 4:
        exit()
    else:
        print("Invalid")
    print("\n\n\n")