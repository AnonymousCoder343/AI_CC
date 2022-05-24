dict_hn = {'A':5,'B':4,'C':2,'D':3,'E':0}

dict_gn = dict(A=dict(B=8, C=5, D=7),

 B=dict(E=2),

 D=dict(E=6),

 C=dict(E=1)

 )

import queue as Q

# from RMP import dict_gn

# from RMP import dict_hn

start = 'A'

goal = 'E'

result = ''

def get_fn(citystr):

 cities = citystr.split(" , ")

 hn = gn = 0

 for ctr in range(0, len(cities) - 1):

 gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]

 hn = dict_hn[cities[len(cities) - 1]]

 return (hn + gn)

def expand(cityq):

 global result


 tot, citystr, thiscity = cityq.get()
 if thiscity == goal:

 result = citystr + " : : " + str(tot)

 return result

 for cty in dict_gn[thiscity]:

 cityq.put((get_fn(citystr + " , " + cty), citystr + " , " + cty, cty))

 expand(cityq)

def main():

 cityq = Q.PriorityQueue()

 thiscity = start

 cityq.put((get_fn(start), start, thiscity))

 expand(cityq)

 print("The A* path with the total is: ")

 print(result)

main()
