# Python program to create a
# GUI mark sheet using tkinter
#packages import
import tkinter as tk
from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess
from PIL import Image, ImageTk
import csv
from tkinter import filedialog, Entry, Label
#time definers
shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ##############################################################################
#commands from gphoto2
clearcmd = ["--folder","/store_00010001/DCIM/100D5100","-R","--delete-all-files"]
triggercmd = ["--trigger-capture"]
downloadcmd = ["--get-all-files"]
previewcmd = ["--capture-preview"]
#FUNCTIONS###############################################
#latt long DM to DECIMA
#lattitude conversion
def lattDMtoDEG():
    global lattdeg
    lattdeg = tk.IntVar()
    if str(latt.get()) == "N":
        lattdeg = var7.get() + (var8.get()/60)
    if str(latt.get()) == "S":
        lattdeg = (-1)*(var7.get() + (var8.get()/60))
    print(lattdeg)
#longitude conversion
def longDMtoDEG():
    global longdeg
    longdeg = tk.IntVar()
    if str(long.get()) == "E":
        longdeg = var9.get() + (var10.get()/60)
    if str(long.get()) == "W":
        longdeg = (-1)*(var9.get() + (var10.get()/60))
    print(longdeg)
#svae data to csv
def saveCSV():
    pic = os.path.basename(str(project_name.get()) + "_S" + str(var4.get()) + "_H" + str(var5.get()) + "_"+ str(number) + ".JPG")
    #print(pic)
    with open("Metadata_" + str(project_name.get()) + ".csv","a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(project_name.get()),str(shot_date),str(shot_time),str(var2.get()),str(var3.get()),str(var4.get()),str(var5.get()),str(var6.get()),str(topbot.get()),
        lattdeg,longdeg,str(var11.get()),str(var12.get()),str(var13.get()),pic,str(var17.get()),str(var18.get()),str(var19.get()),str(var20.get()),str(comments.get())])
#rename the pciture that was taken
def renameFiles():
    for filename in os.listdir("."):
        if filename.startswith("DSC"):
            os.rename(filename, (str(project_name.get()) + "_S" + str(var4.get()) + "_H" + str(var5.get()) + "_"+ str(number) + ".JPG"))
#display a preview of the camera
def previewImage():
    if os.path.exists('capture_preview.jpg'):
        os.remove('capture_preview.jpg')
    gp(previewcmd)
    image = Image.open('capture_preview.jpg')
    image.show()
#sequence to capture image
def captureImages():
    global number
    gp(triggercmd)
    sleep(1)
    gp(downloadcmd)
    gp(clearcmd)
    renameFiles()
    lattDMtoDEG()
    longDMtoDEG()
    saveCSV()
    #print(pic)
    number = number + 1
    piclab = tk.Label(master, text= number).grid(row=2,column=3)
    print(lattdeg)
def raise_frame(frame):
    frame.tkraise()

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    #print(filename)
def CreateSubFolder():
    #if os.path.exists(folder_final)
        #print("folder already created!")
    #else
    os.chdir(str(folder_path.get()))
    os.mkdir(str(project_name.get()))

def FinalFolder():
    CreateSubFolder()
    os.chdir(str(folder_path.get())+"/"+str(project_name.get()))
    print(os.getcwd())
    HeadersCSV()
    raise_frame(master)
    #print(Pic)
    tempo = str(project_name.get())
    projectID = tk.Label(master, text=tempo).grid(row=0,column=1)
    piclab = tk.Label(master, text= number).grid(row=2,column=3)
    pic = tk.StringVar()
def HeadersCSV():
    with open("Metadata_" + str(project_name.get()) + ".csv","a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Project_Name", "Date", "Date_time","Cruise","Ship","Station","Haul","Sample_date_time","top_bot","Lattitude","Longitude","Net_type","Water_depth_m","Tow_speed_kn","PicID","Picture_type","Larvae_size_mm","Larvae_mass_mg","Operator","Comments"])
#def refreshPicID():

#################################################
# creating a new tkinter window
root = tk.Tk()
# assigning a title
root.title("FishCapture")
# specifying geomtery for window size
root.geometry("1000x600")
#logo window
#root.iconbitmap()
#Creating two main frames
Main = tk.Frame(root)
master = tk.Frame(root)
#Define
for frame in (Main,master):
    frame.grid(row=0,column=0,sticky="news")

############################################################################
#MAIN FRAME
#variables pth and project name
folder_path = tk.StringVar()
project_name = tk.StringVar()
tempo = tk.StringVar()
final_path = (str(folder_path.get())+"/"+str(project_name.get()))
pic = tk.StringVar()
#buttons and Labels
#logo
path = "/home/laura/Desktop/gphoto/fish.png"
img = ImageTk.PhotoImage((Image.open(path)).resize((250,250)))
panel = tk.Label(Main, image = img).grid(row=0, column=1)
#labels
Sel = tk.Label(Main, text="The project will be saved in:").grid(row=6, column=0)
CurrentPath = tk.Label(Main, textvariable=folder_path).grid(row=6, column=1)
Pleaseselect = tk.Label(Main, text="Please select a path for the project").grid(row=4, column=1)
LabProj = tk.Label(Main, text="Enter the name of the project").grid(row=2, column=1)
SoftV = tk.Label(Main, text="FishCapture V1.0").grid(row=1, column=1)
#Entries
folder = tk.Entry(Main,textvariable=project_name).grid(row=3, column=1)

#Buttons
CReatefold = tk.Button(Main,height=4, width=10,text="Create Project",command=FinalFolder).grid(row=7, column=2)
#Tomaster = tk.Button(Main,height=4, width=6,text="Create Project",command=lambda:raise_frame(master)).grid(row=0, column=0)
Select_pathButt = tk.Button(Main,text="Browse Folders",command=browse_button).grid(row=5, column=1)






#MASTER frame
#Labels for variables to enter #sample data
lab0 = tk.Label(master, text="Project:").grid(row=0, column=0)
lab1 = tk.Label(master, text="Sample Data").grid(row=1, column=0)
lab2 = tk.Label(master, text="Cruise").grid(row=2, column=0)
lab3 = tk.Label(master, text="Ship").grid(row=3, column=0)
lab4 = tk.Label(master, text="Station").grid(row=4, column=0)
lab5 = tk.Label(master, text="Haul-N").grid(row=5, column=0)
lab6 = tk.Label(master, text="Date and Time (YYYYMMDD-HHMM)").grid(row=6, column=0)
labtopbot = tk.Label(master, text="Top/Bot").grid(row=7, column=0)
lab7 = tk.Label(master, text="Latt. Degree").grid(row=8, column=0)
lab8 = tk.Label(master, text="Latt. Minute").grid(row=9, column=0)
lablatt = tk.Label(master, text="").grid(row=10, column=0)
lab9 = tk.Label(master, text="Long. Degree").grid(row=11, column=0)
lab10 = tk.Label(master, text="Long. Minute").grid(row=12, column=0)
lablong = tk.Label(master, text="").grid(row=13, column=0)
lab11 = tk.Label(master, text="Net Type").grid(row=14, column=0)
lab12 = tk.Label(master, text="Water Depth (m)").grid(row=15, column=0)
lab13 = tk.Label(master, text="Tow Speed (knots)").grid(row=16, column=0)
#labels for fishlarvae
lab14 = tk.Label(master, text="Object Data").grid(row=1, column=2)
lab15 = tk.Label(master, text="PicID").grid(row=2, column=2)
lab16 = tk.Label(master, text="Species").grid(row=3, column=2)
lab17 = tk.Label(master, text="Picture Type").grid(row=4, column=2)
lab18 = tk.Label(master, text="Larvae size (mm)").grid(row=5, column=2)
lab19 = tk.Label(master, text="Larvae mass (mg)").grid(row=6, column=2)
lab20 = tk.Label(master, text="Operator").grid(row=7, column=2)
labComm = tk.Label(master, text="Comments").grid(row=8, column=2)
######Variables where the entered values are stored
#other Variables
number = tk.StringVar()
#lattdeg = tk.IntVar()
#longdeg = tk.IntVar()
number = 0
#sample variables
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
topbot = tk.StringVar()
topbot.set("9999")
#latt
var7 = tk.IntVar()
var7.set("9999")
var8 = tk.DoubleVar()
var8.set("9999")
latt = tk.StringVar()
latt.set("N")
#long
var9 = tk.IntVar()
var9.set("9999")
var10 = tk.DoubleVar()
var10.set("9999")
long = tk.StringVar()
long.set("W")
#others
var11 = tk.StringVar()
var12 = tk.StringVar()
var13 = tk.StringVar()
#larvae variables
var16 = tk.StringVar()
var17 = tk.StringVar()
var17.set("9999")
var18 = tk.StringVar()
var19 = tk.StringVar()
var20 = tk.StringVar()
comments = tk.StringVar()
# cases where users enters data 2 to 13
#sample data
e2 = tk.Entry(master, textvariable=var2).grid(row=2, column=1)
e3 = tk.Entry(master, textvariable=var3).grid(row=3, column=1)
e4 = tk.Entry(master, textvariable=var4).grid(row=4, column=1)
e5 = tk.Entry(master, textvariable=var5).grid(row=5, column=1)
e6 = tk.Entry(master, textvariable=var6).grid(row=6, column=1)
entrytopbot = tk.OptionMenu(master, topbot,"Top","Bot").grid(row=7, column=1)
e7 = tk.Entry(master, textvariable=var7).grid(row=8, column=1)
e8 = tk.Entry(master, textvariable=var8).grid(row=9, column=1)
entrylatt = tk.OptionMenu(master, latt,"N","S").grid(row=10, column=1)
e9 = tk.Entry(master, textvariable=var9).grid(row=11, column=1)
e10 = tk.Entry(master, textvariable=var10).grid(row=12, column=1)
entrylong = tk.OptionMenu(master, long,"W","E").grid(row=13, column=1)
e11 = tk.Entry(master, textvariable=var11).grid(row=14, column=1)
e12 = tk.Entry(master, textvariable=var12).grid(row=15, column=1)
e13 = tk.Entry(master, textvariable=var13).grid(row=16, column=1)
#fishlarvae Data
e16 = tk.Entry(master, textvariable=var16).grid(row=3, column=3)
e17 = tk.OptionMenu(master, var17,"Otolith","Larvae","Prey","Scale","Intestine","Part Larvae","Other").grid(row=4, column=3)
e18 = tk.Entry(master, textvariable=var18).grid(row=5, column=3)
e19 = tk.Entry(master, textvariable=var19).grid(row=6, column=3)
e20 = tk.Entry(master, textvariable=var20).grid(row=7, column=3)
entComm = tk.Entry(master, textvariable=comments).grid(row=8, column=3)

################buttons####
exitButt = tk.Button(master, text="EXIT", command = exit).grid(row=117, column=3)
prevButt = tk.Button(master, text="Preview", command = previewImage).grid(row=17, column=1,padx=10,pady=20)
SavePicButt = tk.Button(master,text="Save Data & Take Picture", command=captureImages).grid(row=17, column=2)






raise_frame(Main)
#run window
root.mainloop()
