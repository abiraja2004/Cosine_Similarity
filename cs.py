import math
import string
def cosine_similarity(v1,v2):
    sumXX, sumYY, sumXY=0,0,0
    for i in range(len(v1)):
        x=v1[i]
        y=v2[i]
        sumXX += x*x
        sumYY += y*y
        sumXY += x*y
    return sumXY/math.sqrt(sumXX*sumYY)

print "Enter two sentences to find cosine similarity among them:"
print "Enter the 1st line:"
s1=raw_input("> ")  #s1=sentence1
print "Enter the 2nd line:"
s2=raw_input("> ")

w1=s1.split()       #w1=words1
w2=s2.split()

a=set(w1)
b=set(w2)

uw=a.union(b)   #uw=unique words
nuw=list(uw)

v1=[]
v2=[]

for x in range(len(nuw)):
    if(nuw[x] in w1):
        v1.append(1)
    else:
        v1.append(0)

for x in range(len(nuw)):
    if(nuw[x] in w2):
        v2.append(1)
    else:
        v2.append(0)

print " "
print "The given two sentences are:\n 1. %s \n 2. %s " %(s1, s2)
print " "
print "The unique words involving both the sentences are:"
print nuw
print " "
print "Cosine Similarity of the given two sentences is ", cosine_similarity(v1,v2)
print " "
print "*"*30
threshold=cosine_similarity(v1,v2)
if threshold > 0.5:
    print "The sentences are very similar."
else:
    print "The sentences are less similar."
print "*"*30
print"\n"

print "If you would like to see the corresponding vectors"
print nuw
print v1
print v2
