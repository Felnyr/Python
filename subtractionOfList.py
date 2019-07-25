# Dana jest lista liczb. 
# Program ma na jej podstawie wyznaczyć róż-nice między wyrazem pierwszym a drugim, 
# drugim a trzecim, itd. aż do końca,po czym powiedzieć, 
# jaka wartość spośród różnic była najmniejsza, największa,najbliższa zera.

# Given an array of numers, 
# program calculates diffrences between first, secound, third, element till the end of list
# and prints the diffrences: max, min and nearest to zero from all the values


x = [4,7,7,55,335,2,45,2,3]
q = []
for i in range( len(x) - 1 ):
    z = x[i+1] - x[i]
    q.append(z)
q.sort()
print(q)
print(q[0])
print(q[len(q) - 1])


