
# method that reads data from file
#params : input :mat, file
#         output: number of towns-INT, town1-SourceTown -INT,town2-DestinationTown -INT
def readFromFile(mat, file):
  
    file = open(file, 'r')
    
    numberTowns = int(file.readline())
    m=numberTowns

    while m!=0:
        lineList = []
        line = file.readline()
        valuesL = line.split(',')
        
        for val in  valuesL:
            valInt=int(val)
            lineList.append(valInt)

        mat.append(lineList)
        m=m-1

    town1,town2= int(file.readline()), int(file.readline())
  

    return numberTowns,town1,town2



# method that returns the minimal path from source to destination
#params : input :mat, numberTowns, source,destination
#         output:len(visited)-number of visited towns-INT, visited-vector, sum- sum of costs-INT

def minPathFromStoD(mat, numberTowns, source, destination):
    
    visited = [source] 
    Min=[]
    sum = 0
    m=numberTowns
    while m!=0:
        length=len(visited) 
        if length!=numberTowns:
            Min = distanceMinimal(numberTowns, mat[visited[-1] - 1], visited)
            sum =sum+Min[0]
            visited.append(Min[1])

        if (visited[-1] == destination): 
               break
        m=m-1

    if(source==destination):
        sum =sum+ mat[visited[-1] - 1][visited[0] - 1]

    return len(visited),visited,sum




# method that returns the town  with the minimal distance(cost), and the minimal cost for the last visited node
#params : input :numberTown, cost- vector of distances for the last visited node
#         output:Min- vector, Min[0]-minimal cost(distance), Min[1]-index of the minimal cost

def distanceMinimal(numberTowns, cost, visited):
    minCost =10000000
    index=0
    minIndex = -1
   
   
    while index!=numberTowns:
        if cost[index] < minCost and cost[index] != 0:
            if  index + 1 not in visited :
                minCost,minIndex = cost[index],index+1
             
        index=index+1
    Min=[]
    Min.append(minCost)
    Min.append(minIndex)
    return Min

def writeToFile(file2, nr1,vis1,sum1,nr2,vis2,sum2):

    file2.write(str(nr1))
    file2.write('\n')
    file2.write(str(vis1))
    file2.write('\n')
    file2.write(str(sum1))
    file2.write('\n')
    file2.write(str(nr2))
    file2.write('\n')
    file2.write(str(vis2))
    file2.write('\n')
    file2.write(str(sum2))
    file2.write('\n')



  
   
def main():
    #file = 'easy_01_tsp.txt'
    #file = 'easy_03_tsp.txt'
    #file = 'medium_01_tsp.txt'
    file = 'hard_01_tsp.txt'
    minimSum=100000
    mat = []
    path=[]
    
    numberTowns,s,d = readFromFile(mat, file)


    print(minPathFromStoD(mat, numberTowns,1,1))
    print(minPathFromStoD(mat, numberTowns,s,d))


    file2='easy_01_sol.txt'
    file2 = open(file2, 'w', encoding="utf-8")

 
    nr1,vis1,sum1=minPathFromStoD(mat, numberTowns,1,1)
    nr2,vis2,sum2=minPathFromStoD(mat, numberTowns,s,d)
    writeToFile(file2, nr1,vis1,sum1,nr2,vis2,sum2 )
   
main()