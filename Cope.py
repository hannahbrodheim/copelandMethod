#!/usr/bin/python
import sys
import csv

class Ballot:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, votes):
      self.votes = votes
      Ballot.empCount += 1
   
   def displayCount(self):
     print "Total Ballots %d" % Ballot.empCount

   def displayBallot(self):
      i = 0
      a = ""
      while(i < len(self.votes)):
         a += " Vote "+ str(i+1)+" "+str(self.votes[i])
         i += 1
      return a

   "Return 1 if the first candidate is preferred, return -1 if the second candidate is preferred"
   def compare(self, ca, cb):
      for v in self.votes:
         if(v == ca):
            return 1
         if(v == cb):
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
               if(ci == cj):
                  candidates[i][1] += .5
                  candidates[j][1] += .5
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
            tiewinner = ""
            curmax = score
            curwinner = c
        else:
            if score == curmax:
                tie = True
                tiewinner += " and " +c
    if(tie):
        return "There was a tie between "+curwinner +tiewinner+" they won "+ str(curmax)+ " contests, your problem now I'm afraid"
    else:
        return curwinner+" is the winner"




ballots = []
def processBallot(a, ref):
   i = 0
   ab = ['a']*len(a)
   while(i < len(a)):
      ab[int(a[i])-1] = ref[i]
      i +=1
   return Ballot(ab)


def mergeLists(a,b):
   c = []
   i = 0
   while ( i < len(a)):
      c.append([a[i],b[i]])
      i+=1
   return c
ref = []
candidates = []
f = open("ballots.csv", 'rb')
try:
   reader = csv.reader(f)
   i = 0
   for row in reader:
      if(i==0):
         ref = row
         candidates = mergeLists(row, [0]*len(row))
      else:
         ballots.append(processBallot(row, ref))
      i = 1
finally:
   f.close()



for b in ballots:
    b.displayBallot()
runCopland(candidates, ballots)

fo = open("ElectionResults.txt", "w+")
"fo.write( candidates)"
fo.write( getWinner(candidates))
fo.write('\n')
fo.write( "Total Ballots %d" % Ballot.empCount)
fo.write('\n')
fo.write( "Votes were "+ str(candidates))
fo.write('\n')
fo.write('\n')
fo.write("Ballot received: ")
fo.write('\n')
for b in ballots:
    fo.write(str(b.displayBallot()))
    fo.write('\n')
fo.close()

