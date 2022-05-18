# BFS algorithm in Python
graph = {1 : [0,3],0 : [10,2],3 : [5,4],10 : [63,65],2 : [],5 : [],4: []}
def fun(node,goal,graph):
    q=[]
    q.append(node)
    print(node)
    while q:
        s=q.pop(0)
        for i in graph[s]:
            if i != goal:
                print(i)
                q.append(i)
            else:
                print(i)
                return False

fun(1,63,graph)
