# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

path=[]

def minimax (curDepth, nodeIndex,maxTurn, scores,targetDepth):
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        left=minimax(curDepth + 1, nodeIndex * 2,False, scores, targetDepth)
        right=minimax(curDepth + 1, nodeIndex * 2 + 1,False, scores, targetDepth)
        return max(left,right)
    else:
        left=minimax(curDepth + 1, nodeIndex * 2,True, scores, targetDepth)
        right=minimax(curDepth + 1, nodeIndex * 2 + 1,True, scores, targetDepth)
        return min(left,right)

    
# Driver code
scores = [int(item) for item in input("Enter Even number of Leaf Node Values : ").split()]

treeDepth = math.log(len(scores), 3) 
# print(treeDepth)
print("The optimal value is : ", end = "")
optimal=minimax(0, 0, True, scores, treeDepth)
print(optimal)
for i in range(len(scores)):
    if (scores[i]==optimal):
        break;
x=pow(3,treeDepth)+i
path.append(int(x))
while(x>=3):
    x//=3
    path.append(int(x))
print("Optimal path: ")
print(*path , sep=' -> ')
