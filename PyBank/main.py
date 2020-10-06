#First, importing & source
import os
import csv
resourcepath= os.path.join('Resources','budget_data.csv')

#declaring
Date=[]
Budget=0
TotalChanges=[]
Average=[]



#The reading
with open(resourcepath,"r") as mainfile:
    filereader=csv.reader(mainfile, delimiter=",")
    
    header=next(filereader)
    previous_row=next(filereader)
    count=1
    Budget=int(previous_row[1])
    great_increase=["",-1000000000000000]
    min_decrease=["",10000000000000000]

    #now, the iteration
    for row in filereader:
        change=int(row[1])-int(previous_row[1])
        TotalChanges.append(change)
        if(great_increase[1]<change):
            great_increase[1]=change
            great_increase[0]=row[0]
        if(min_decrease[1]>change):
            min_decrease[1]=change
            min_decrease[0]=row[0]
        count=count+1
        previous_row=row
        Budget=Budget+int(row[1])


  
# print(f"""Financial Analysis
# -----------------------------
# Total Months: {count}
# Total: ${Budget}
# Average Change: ${round(sum(TotalChanges)/len(TotalChanges),2)}
# Greatest Increase in Profits: {great_increase[0]} (${great_increase[1]})
# Greatest Decrease in profits: {min_decrease[0]} (${min_decrease[1]})

# """)

output_path = os.path.join("Analysis", "Financial Analysis.txt")

with open(output_path,'w') as outfile:
    outfile.write(f"""Financial Analysis
-----------------------------
Total Months: {count}
Total: ${(Budget)}
Average Change: ${round(sum(TotalChanges)/len(TotalChanges),2)}
Greatest Increase in Profits: {great_increase[0]} (${great_increase[1]})
Greatest Decrease in profits: {min_decrease[0]} (${min_decrease[1]})

""")