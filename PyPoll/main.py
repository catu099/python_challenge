#First the importing & source
import os
import csv
resourcepath= os.path.join('Resources','election_data.csv')

#declaring
Voter_ID=[]
County=[]
Candidate=[]



#The reading
with open(resourcepath,"r") as mainfile:
    filereader=csv.reader(mainfile, delimiter=",")
    
    header=next(filereader)
    
    count=0
    Total_Khan_voters=0
    Total_Correy_voters=0
    Total_Li_voters=0
    Total_Otooley_voters=0
    


    #The iteration
    for row in filereader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        count=count+1
            
        row_candidate=row[2]
        if row_candidate == "Khan":
            Total_Khan_voters=(Total_Khan_voters+1)
        if row_candidate == "Correy":
            Total_Correy_voters=(Total_Correy_voters+1)
        if row_candidate == "Li":
            Total_Li_voters=(Total_Li_voters+1)
        if row_candidate == "O'Tooley":
            Total_Otooley_voters=(Total_Otooley_voters+1)



    #winner:
    if Total_Khan_voters>Total_Correy_voters and Total_Khan_voters>Total_Li_voters and Total_Khan_voters>Total_Otooley_voters:
        winner="Khan"
    if Total_Correy_voters>Total_Khan_voters and Total_Correy_voters>Total_Li_voters and Total_Correy_voters>Total_Otooley_voters:
        winner="Correy"
    if Total_Li_voters>Total_Khan_voters and Total_Li_voters>Total_Correy_voters and Total_Li_voters>Total_Otooley_voters:
        winner="Li"
    if Total_Otooley_voters>Total_Correy_voters and Total_Otooley_voters>Total_Li_voters and Total_Otooley_voters>Total_Khan_voters:
        winner="O'Tooley"

# print(f"""Election Results
# -----------------------------
# Total Votes: {count}
# -----------------------------
# Khan: {"{:.3f}".format(Total_Khan_voters/count*100)}%  ({Total_Khan_voters})
# Correy: {"{:.3f}".format(Total_Correy_voters/count*100)}%  ({Total_Correy_voters})
# Li: {"{:.3f}".format(Total_Li_voters/count*100)}%  ({Total_Li_voters})
# O'Tooley: {"{:.3f}".format(Total_Otooley_voters/count*100)}%  ({Total_Otooley_voters})
# -----------------------------
# Winner: {winner}
# -----------------------------
#  """)

output_path = os.path.join("Analysis", "Election Results.txt")

with open(output_path,'w') as outfile:
    outfile.write(f"""Election Results
-----------------------------
Total Votes: {count}
-----------------------------
Khan: {"{:.3f}".format(Total_Khan_voters/count*100)}%  ({Total_Khan_voters})
Correy: {"{:.3f}".format(Total_Correy_voters/count*100)}%  ({Total_Correy_voters})
Li: {"{:.3f}".format(Total_Li_voters/count*100)}%  ({Total_Li_voters})
O'Tooley: {"{:.3f}".format(Total_Otooley_voters/count*100)}%  ({Total_Otooley_voters})
-----------------------------
Winner: {winner}
-----------------------------
 """)