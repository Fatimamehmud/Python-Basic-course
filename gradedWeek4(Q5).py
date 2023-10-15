# Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are increased by 5.
#Note this is not an accumulator pattern problem, but its a good review.

numbs = [5, 10, 15, 20, 25]
numbs[0]=5+5
numbs[1]=10+5
numbs[2]=15+5
numbs[3]=20+5
numbs[4]=25+5
#or
numbs = [5, 10, 15, 20, 25]
newlist=[]

for i in range(len(numbs)):
    newlist.append(numbs[i]+5)
print(newlist)

#or
numbs = [5, 10, 15, 20, 25]
x=0
for numb in numbs:
    numbs[x]=numb+5
    x+=1
print(numbs)
