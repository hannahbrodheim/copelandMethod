#!/usr/bin/python
from Tkinter import *
import tkMessageBox 
import sys
class Ballot:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, first, second, third):
      self.first = first
      self.second = second
      self.third = third
      Ballot.empCount += 1
   
   def displayCount(self):
     print "Total Ballots %d" % Ballot.empCount

   def displayBallot(self):
      return "First vote for: ", self.first,  ", Second vote for: ", self.second, ", Third vote for: ", self.third

   "Return 1 if the first candidate is preferred, return -1 if the second candidate is preferred"
   def compare(self, ca, cb):
       if(ca == self.first):
           return 1
       else:
           if (cb == self.first):
               return -1
           else:
               if(ca == self.second):
                   return 1
               else:
                   return -1
        

def runCopland(candidates, ballots):
    i = 0
    while (i < len(candidates) - 1):
        j = i+1

        while ( j < len(candidates)):
            ci = 0
            cj = 0
            for b in ballots:
                if(1 == b.compare(candidates[i][0], candidates[j][0])):
                    ci +=1
                else:
                    cj+=1
            if (ci > cj):
                candidates[i][1] += 1
            else:
                candidates[j][1] += 1
            j+=1
        i+=1

def getWinner(candidates):
    curmax = 0
    curwinner = ""
    tiewinner = ""
    tie = False
    for (c, score) in candidates:
        if (score > curmax):
            tie = False
            curmax = score
            curwinner = c
        else:
            if score == curmax:
                tie = True
                tiewinner = c
    if(tie):
        return "There was a tie between "+curwinner +" and "+tiewinner+" they both won "+ str(curmax)+ " contests, your problem now I'm afraid"
    else:
        return curwinner+" is the winner"
ballots = []
candidates = [["M",0], ["G",0], ["Z", 0]]





top = Tk()

def readIn():
    if ((varfirst.get() == varsecond.get() or varfirst.get() == varthird.get() or varsecond.get() == varthird.get())):
        tkMessageBox.showerror("Double Match", "Same candidate selected multiple times")
    else:
        print "Selected Rankings: First " + str(varfirst.get()) + " Second "+ str(varsecond.get()) + " Third " + str(varthird.get())
        ballots.append(Ballot (varfirst.get(), varsecond.get(), varthird.get()))
        R1.select()
        R1S.select()
        R1T.select()

def endProgram():
    top.quit()
newB = Button (top, text="Submit Ballot", command = readIn)
newB.pack()

varfirst = StringVar()
label1 = Label(top)
label1.config(text="Top Candidate")
label1.pack()
R1 = Radiobutton(top, text="M", variable=varfirst, value="M")
R1.pack (anchor = W)

R2 = Radiobutton(top, text="G", variable=varfirst, value="G")
R2.pack (anchor = W)

R3 = Radiobutton(top, text="Z", variable=varfirst, value="Z")
R3.pack (anchor = W)
varsecond = StringVar()
label2 = Label(top)
label2.config(text="Second Candidate")
label2.pack()
R1S = Radiobutton(top, text="M", variable=varsecond, value="M")
R1S.pack (anchor = W)

R2S = Radiobutton(top, text="G", variable=varsecond, value="G")
R2S.pack (anchor = W)

R3S = Radiobutton(top, text="Z", variable=varsecond, value="Z")
R3S.pack (anchor = W)

varthird = StringVar()
label3 = Label(top)
label3.config(text="Third Candidate")
label3.pack()
R1T = Radiobutton(top, text="M", variable=varthird, value="M")
R1T.pack (anchor = W)

R2T = Radiobutton(top, text="G", variable=varthird, value="G")
R2T.pack (anchor = W)

R3T = Radiobutton(top, text="Z", variable=varthird, value="Z")
R3T.pack (anchor = W)

endB = Button (top, text="All ballots are in", command = endProgram)
endB.pack()
top.mainloop()


for b in ballots:
    b.displayBallot()
runCopland(candidates, ballots)

fo = open("trialelection.txt", "w+")
"fo.write( candidates)"
fo.write( getWinner(candidates))
fo.write('\n')
fo.write( "Total Ballots %d" % Ballot.empCount)
fo.write('\n')
fo.write('\n')
fo.write('\n')
fo.write("Ballot received: ")
fo.write('\n')
for b in ballots:
    fo.write(str(b.displayBallot()))
    fo.write('\n')
fo.close()
