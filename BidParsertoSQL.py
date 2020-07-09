


import os
import datetime
import time

#File Dependencies
#import gui
#import module1.py
import interface






PREFIX = "INSERT INTO PS_QB_BID_MASTER VALUES("
SUFFIX = ");\n"


#all of this will be added to the session manager class
mark_bidEntry = False
mark_BidAlertNo = False
mark_AgencyBidNo = False
mark_Title = False
mark_ReceivedDate = False
mark_CloseDate = False
mark_DeliveryPoint = False
mark_DeliveryDate = False
mark_Specifications = False
mark_ProductCodes = False
mark_IssuingAgency = False
mark_UsingAgency = False
mark_State = False
mark_AgencyType = False
mark_Contact = False
mark_Phone = False
mark_Fax = False
mark_Email = False

bid = "' ',"
BidAlertNo = "' ',"
AgencyBidNo = "' ',"
Title= "' ',"
ReceivedDate = "' ',"
CloseDate = "' ',"
DeliveryPoint= "' ',"
DeliveryDate= "' ',"
Specifications = "' ',"
ProductCodes = "' ',"
IssuingAgency = "' ',"
UsingAgency= "' ',"
State = "' ',"
AgencyType = "' ',"
Contact = "' ',"
Phone= "' ',"
Fax= "' ',"
Email ="' '"


bidAlertMarker1 = False
bidAlertMarker2 = False
bidAlertMarker3 = False
bidAlertMarker4 = False

bidSheetDate = ""
markbidSheetDate = 0
markReset = False
initialDateMarker = True

file_selection = 0



from html.parser import HTMLParser


#in progress class that will eventually manage all global variables into a single class that controls the session
class sessionManager:
    
    mark_bidEntry = False
    mark_BidAlertNo = False
    mark_AgencyBidNo = False
    mark_Title = False
    mark_ReceivedDate = False
    mark_CloseDate = False
    mark_DeliveryPoint = False
    mark_DeliveryDate = False
    mark_Specifications = False
    mark_ProductCodes = False
    mark_IssuingAgency = False
    mark_UsingAgency = False
    mark_State = False
    mark_AgencyType = False
    mark_Contact = False
    mark_Phone = False
    mark_Fax = False
    mark_Email = False

    def __init__(self):
        self.ohio = None
        self.bidSheetDate = None

    def test(self):
        print(self.ohio)
    
    def reset(self):
        self.mark_bidEntry = False
        self.mark_BidAlertNo = False
        self.mark_AgencyBidNo = False
        self.mark_Title = False
        self.mark_ReceivedDate = False
        self.mark_CloseDate = False
        self.mark_DeliveryPoint = False
        self.mark_DeliveryDate = False
        self.mark_Specifications = False
        self.mark_ProductCodes = False
        self.mark_IssuingAgency = False
        self.mark_UsingAgency = False
        self.mark_State = False
        self.mark_AgencyType = False
        self.mark_Contact = False
        self.mark_Phone = False
        self.mark_Fax = False
        self.mark_Email = False



    def test2(self):
        print(self.mark_bidEntry)


       #A subclass of HTMLParser and override the handler methods

class MyHTMLParser(HTMLParser):

  
    def handle_data(self, data):
        global mark_bidEntry
        global mark_BidAlertNo
        global mark_AgencyBidNo
        global mark_Title
        global mark_ReceivedDate
        global mark_CloseDate
        global mark_DeliveryPoint
        global mark_DeliveryDate
        global mark_Specifications
        global mark_ProductCodes

        global mark_IssuingAgency
        global mark_UsingAgency
        global mark_State
        global mark_AgencyType
        global mark_Contact
        global mark_Phone
        global mark_Fax
        global mark_Email

        global bidAlertMarker1
        global bidAlertMarker2
        global bidAlertMarker3
        global bidAlertMarker4

        global bid
        global BidAlertNo 
        global AgencyBidNo 
        global Title
        global ReceivedDate 
        global CloseDate 
        global DeliveryPoint
        global DeliveryDate
        global Specifications 
        global ProductCodes 
        global IssuingAgency 
        global UsingAgency
        global State 
        global AgencyType 
        global Contact 
        global Phone
        global Fax
        global Email 

        global markReset

        global bidSheetDate
        global markbidSheetDate


        if (data.isspace()):
          return
          print ("Encountered some text data:", data)
        
        elif(markReset ==True):
            bid = "' ',"
            BidAlertNo = "' ',"
            AgencyBidNo = "' ',"
            Title = "' ',"
            ReceivedDate = "'',"
            CloseDate = "'',"
            DeliveryPoint = "' ',"
            DeliveryDate = "'',"
            Specifications = "' ',"
            ProductCodes ="' ',"
            IssuingAgency = "' ',"
            UsingAgency = "' ',"
            State = "' ',"
            mAgencyType = "' ',"
            Contact = "' ',"
            Phone = "' ',"
            Fax = "' ',"
            Email = "' '"
            markReset = False


        elif(bidAlertMarker1 == True and data == "Bid Alerts For Today's Bid Matches"):
            mark_bidEntry = False
            mark_BidAlertNo = False
            mark_AgencyBidNo = False
            mark_Title = False
            mark_ReceivedDate = False
            mark_CloseDate = False
            mark_DeliveryPoint = False
            mark_DeliveryDate = False
            mark_Specifications = False
            mark_ProductCodes = False
            mark_IssuingAgency = False
            mark_UsingAgency = False
            mark_State = False
            mark_AgencyType = False
            mark_Contact = False
            mark_Phone = False
            mark_Fax = False
            mark_Email = False
            bidAlertMarker2 = True
            resetCases()

            #sets up first trigger before parsing
        elif(data == "Bid Alerts For Today's Bid Matches"):  
            bidAlertMarker1 = True
            #print(bidAlertMarker1)            

            #we are done parsing
        elif(bidAlertMarker2 == True and data == "Bid Alerts For Today's Amendment Matches"):
            bidAlertMarker1 = False
            bidAlertMarker2 = False

            #enables parsing into variables
        elif(bidAlertMarker2 == True and "Bid Information" in data and bid !="' ',"):
            finalOutput()
            markReset = True


            #this is what the file will be named
        elif(markbidSheetDate == 2):
            bidSheetDate = data
            print("THE DATE OF THIS SHEET IS: " + data)
            markbidSheetDate = markbidSheetDate + 1
            outputfile = open("output\\"+ "EXPORT_" + bidSheetDate + ".txt", 'w', encoding="utf-8")

        #1
        elif(mark_BidAlertNo == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                bid = "'"+data+"'"+", "
                resetCases()
                mark_BidAlertNo = False

            else:
                bid = "'"+data+"'"+", "
                resetCases()
                mark_BidAlertNo = False
           # session.markBidAlertNo = False
        

        #2  
        elif(mark_AgencyBidNo == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                AgencyBidNo = "'" + data + "'"+", "
                resetCases()
                mark_AgencyBidNo = False   
            else:
              AgencyBidNo = "'" + data + "'"+", "
              resetCases()
              mark_AgencyBidNo = False
            #sessionManager.mark_AgencyBidNo = False
        #3
        elif(mark_Title == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                data = data.replace("'", "")
                data = data.replace(":", "")
                Title = "'" + data + "'" +", "


                resetCases()
                mark_Title = False

            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                Title = "'" + data + "'" +", "
                resetCases()
                mark_Title = False
            #sessionManager.mark_Title = False
        #4
        elif(mark_ReceivedDate == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                ReceivedDate = "CONVERT(DATETIME," +"'"+ data +"'"+ "), "
                resetCases()
                mark_ReceivedDate = False   

            else:
                ReceivedDate = "CONVERT(DATETIME," +"'"+ data +"'"+ "), "
                resetCases()
                mark_ReceivedDate = False   
            #sessionManager.mark_ReceivedDate = False

        #5
        elif(mark_CloseDate == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                CloseDate = "'"+data + "'" +", "
                resetCases()
                mark_CloseDate = False

            else:
                CloseDate = "'"+data + "'" +", "
                resetCases()
                mark_CloseDate = False
           # sessionManager.markCloseDate = False
        #6
        elif(mark_DeliveryPoint == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                data = data.replace("'", "")
                data = data.replace(':', '')
                DeliveryPoint = "'"+data + "'" +", "
                resetCases()
                mark_DeliveryPoint = False

            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                DeliveryPoint = "'"+data + "'" +", "
                resetCases()
                mark_DeliveryPoint = False
          #  sessionManager.mark_DeliveryPoint = False
        #7
        elif(mark_DeliveryDate == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                data = data.replace("'", "")
                data = data.replace(':', '')
                DeliveryDate = "'"+data + "'" +", "
                resetCases()
                mark_DeliveryDate = False

            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                DeliveryDate = "'"+data + "'" +", "
                resetCases()
                mark_DeliveryDate = False
           # sessionManager.mark_DeliveryDate = False
        #8
        elif(mark_Specifications == True and bidAlertMarker2 == True):
            print(data)
            if len(data) >= 250:
                data = data.replace("'", "")
                data = data.replace(':', '')
                trunacteddata = data[:250]
                Specifications = "'"+ trunacteddata+ "'"+", "
                resetCases()
                mark_Specifications = False

            else:
                data = data.replace("'", '')
                data = data.replace(':', '')
                Specifications = "'"+ data+ "'"+", "
                resetCases()
                mark_Specifications = False
               # sessionManager = mark_Specifications = False

        #9
        elif(mark_ProductCodes == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                data = data.replace("'", "")
                data = data.replace(':', '')
                ProductCodes ="'"+ data +"'"+", "
                resetCases()
                mark_ProductCodes = False

            else:
                ProductCodes ="'"+ data +"'"+", "
                resetCases()
                mark_ProductCodes = False
          #  sessionManager.markmark_ProductCodes = False
        #10
        elif(mark_IssuingAgency == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                IssuingAgency = "'"+ data + "'"+", "
                resetCases()
                mark_IssuingAgency = False

            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                IssuingAgency = "'"+ data + "'"+", "
                resetCases()
                mark_IssuingAgency = False
             #   sessionManager.mark_IssuingAgency = False
        #11
        elif(mark_UsingAgency == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                UsingAgency = "'"+ data + "'"+", "
                resetCases()
                mark_UsingAgency = False
            else:
                UsingAgency = "'"+ data + "'"+", "
                resetCases()
                mark_UsingAgency = False
             #   sessionManager.mark_UsingAgency = False
        #12
        elif(mark_State == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                State = "'" + data + "'"+", "
                resetCases()
                mark_State = False
            else:
                State = "'" + data + "'"+", "
                resetCases()
                mark_State = False
              #  sessionManager.mark_State = False
       #13
        elif(mark_AgencyType == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data[:250]
                data = data.replace("'", "")
                data = data.replace(':', '')
                AgencyType = "'" + data + "'"+", "
                resetCases()
                mark_AgencyType = False
            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                AgencyType = "'" + data + "'"+", "
                resetCases()
                mark_AgencyType = False
         #   sessionManager.mark_AgencyType = False
        #14
        elif(mark_Contact == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                Contact = "'" + data + "'"+", "
                resetCases()
                mark_Contact = False
            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                Contact = "'" + data + "'"+", "
                resetCases()
                mark_Contact = False
        #15
        elif(mark_Phone == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                Phone = "'" + data + "'"+", "
                resetCases()
                mark_Phone = False
            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                Phone = "'" + data + "'"+", "
                resetCases()
                mark_Phone = False
        #16
        elif(mark_Fax == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                Fax = "'" + data + "'"+", "
                resetCases()
                mark_Fax = False
            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                Fax = "'" + data + "'"+", "
                resetCases()
                mark_Fax = False
        #17
        elif(mark_Email == True and bidAlertMarker2 == True):
            if(len(data) > 250):
                data = data.replace("'", "")
                data = data.replace(':', '')
                data = data[:250]
                Email = "'" + data + "'"
                resetCases()
                mark_Email = False
            else:
                data = data.replace("'", "")
                data = data.replace(':', '')
                Email = "'" + data + "'"
                resetCases()
                mark_Email = False

        #Checks string and assigns booleans


        elif("Bid Alert Bulletin" in data):
           markbidSheetDate = markbidSheetDate + 1

        elif(data == "Bid Information"):
            mark_bidEntry = True

        elif("Alert No.:" in data):
            mark_BidAlertNo = True

        elif("Bid No.:" in data):
            mark_AgencyBidNo = True

        elif("Title:" in data):
            mark_Title = True

        elif("Received Date" in data):
            mark_ReceivedDate = True

        elif("Close" and  "Date" in data):
            mark_CloseDate = True

        elif("Delivery" and "Point:" in data):
            mark_DeliveryPoint = True

        elif("Delivery" in data and "Date:" in data):
            mark_DeliveryDate = True

        elif("Specifications" in data):
            mark_Specifications = True

        elif("Product Code(s):" in data):
            mark_ProductCodes = True

        elif("Using" in data and "Agency:" in data):
            mark_UsingAgency = True

        elif("Issuing" in data and "Agency:" in data):
            mark_IssuingAgency = True

        elif("State:" in data):
            mark_State = True

        elif("Agency" and "Type:" in data):
            mark_AgencyType = True

        elif("Contact" in data):
            mark_Contact = True

        elif("Phone" in data):
            mark_Phone = True

        elif("Fax" in data):
            mark_Fax = True

        elif("Email" in data):
            mark_Email = True

               





def main():

  global file_selection 



  #migrate to gui
  dir = os.listdir("resources") 

  if len(dir) == 0: 
    print("Empty directory... Please place a bid file before running") 
  else: 
    arr = os.listdir('resources')
    print("Displaying files for parsing")
    for i in range(len(arr)):

        print(i, "-", arr[i])
    selection = input("Please enter the number associated with the file you wish to parse...\n")
    time.sleep(1)
    while int(selection) > len(arr):
        selection = input("Please enter the number associated with the file you wish to parse...\n")
    else:
        print(arr[int(selection)])

    file_selection = arr[int(selection)]
    print(arr[int(selection)])

  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
    
  # open the sample HTML file and read it
  file = open("resources/"+file_selection)

  if file.mode == "r":
    contents = file.read() # read the entire file
    parser.feed(contents)

  print("Parisng is complete")


    
    #outdated function which will be merged into new class file   
def fileAdjustment():
    print(os.getcwd())
    newfilename = "output" + bidSheetDate +".txt"
    print(newfilename)
    original = "output.txt"
    print(original)
    if(os.path.exists("output.txt") == True):
        print("Its here")
    elif(os.path.exists("output.txt") == False):
        print("nothing here")


def checkStatus():
        print(">>>>>RUNNING DIAGNOSTIC:<<<<<<")
        print("Bid entry:", mark_bidEntry)
        print("Bid Alert No:",mark_BidAlertNo)
        print("Agency Bid No:", mark_AgencyBidNo)
        print("Title:",mark_Title)
        print("Recevied Date:",mark_ReceivedDate)
        print("Close Date:",mark_CloseDate)
        print("Delivery point:",mark_DeliveryPoint)
        print("Delivery Date:",mark_DeliveryDate)
        print("Specifications:",mark_Specifications)
        print("Product Codes:",mark_ProductCodes)
        print("Issuing Agency:",mark_IssuingAgency)
        print("Using Agency:",mark_UsingAgency)
        print("State:", mark_State)
        print("Agency Type:",mark_AgencyType)
        print("Phone:",mark_Phone)
        print("Fax:",mark_Fax)
        print("Email:",mark_Email)
    

def finalOutput():

     outputfile = open("output\\"+ "EXPORT_" + bidSheetDate + ".txt", 'a', encoding="utf-8")
     output = PREFIX + bid + AgencyBidNo + Title + ReceivedDate + CloseDate + DeliveryPoint + DeliveryDate + Specifications + ProductCodes + IssuingAgency + UsingAgency + State + AgencyType + Contact + Phone + Fax + Email + SUFFIX
     print(output)
     outputfile.write(output)
     outputfile.close()


def resetCases(): 
         mark_BidAlertNo = False
         mark_AgencyBidNo = False 
         mark_Title = False
         mark_ReceivedDate = False
         mark_CloseDate= False
         mark_DeliveryPoint = False
         mark_DeliveryDate= False
         mark_Specifications = False
         mark_ProductCodes = False
         mark_IssuingAgency = False
         mark_UsingAgency = False
         mark_State = False
         mark_AgencyType = False
         mark_Contact = False
         mark_Phone = False
         mark_Fax = False
         mark_Email = False


import tkinter.filedialog as filedialog
import tkinter as tk


filepath = None

main_window = tk.Tk()

def input():
    global filepath
    input_path = tk.filedialog.askopenfilename()
    filepath = input_path
    print(input_path)
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    print(input_path)


def output():
    path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  
    input_entry.insert(0, path)  


top_frame = tk.Frame(main_window)
bottom_frame = tk.Frame(main_window)
line = tk.Frame(main_window, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)


def startparse():
  parser = MyHTMLParser()

  file = open(filepath)

  if file.mode == "r":
    contents = file.read() # read the entire file
    parser.feed(contents)

  print("Parisng is complete")
  
  print(filepath)



begin_button = tk.Button(bottom_frame, text='Begin parsing', command =startparse)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)



begin_button.pack(pady=20, fill=tk.X)

#begins listening for events
main_window.mainloop()


#if __name__ == "__main__":
#  main()
  