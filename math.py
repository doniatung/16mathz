# Team NintendoDS (Donia Tung & Samantha Ngo)
# SoftDev2 pd7
#K#16 -- Ready, Set, Math
#2018-04-26


def union(setA, setB):
    return [x for x in setA if x in setB or setA] + [x for x in setB if x not in setA]

def intersection(setA, setB):
    return [x for x in setA if x in setB]

#returns all members of the first set that are not in the second set
def setDiff(setA, setB):
    return [x for x in setA if x not in setB]

def symDiff(setA, setB):
    return setDiff(setA,setB) + setDiff(setB, setA)

def cartProd(setA, setB):

    return [(x,y) for x in setA for y in setB]



setA = "123456"
setB = "456789"
print union(setA, setB)#['1', '2', '3', '4', '5', '6', '7', '8', '9']
print intersection(setA, setB) #['4', '5', '6']
print setDiff(setA, setB) #['1', '2', '3']
print setDiff(setB, setA)#['7', '8', '9']
print symDiff(setA, setB)#['1', '2', '3', '7', '8', '9']
print cartProd(setA, setB)#['1', '2', '3', '7', '8', '9']
