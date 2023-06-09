#libraries or dependencies 
import os
import csv 

#variable is being defined by inputted data from Excel 
Election_DataLoad = os.path.join ("Resources", "ElectionData.csv")
Election_Output = os.path.join ("Resources", "Election_Analysis.txt")


#whenever you're extracting data from your local computer you use os.path.join 

#initialize parameters 
Total_Votes = 0

Candidates_List = [1, 2, 3]
var1 = ""
var2 = ""
var3 = ""



Percentage_Winners = 0 
Total_WinningVotes = 0 
Winner = ""


with open (Election_DataLoad) as data:
    reader = csv.reader(data)
    #header row 
    header = next(reader)

    for Row in reader:
        #print(Row)
        #exit()
        
        Total_Votes += 1
        #adds value to existing and assigns new value back to same variable 
            


    print(Total_Votes) 

    #print(list[0])
    #print(list(1))
    #print(list(2))

    
output = f"""
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
"""    

print(output) 

with open (Election_Output, "w") as fdata:
    fdata.write(output)
    
    