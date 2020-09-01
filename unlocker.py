position={}
def solve_unlock(locker,rotate,rows,cols):
    k,l=0,0
    layer_number=1
    while(k<rows and l<cols):
        layer=[]
        index=0
        for i in range(l,cols):
            layer.append(locker[k][i])
            position[index]=[k,i]
            index+=1
        k+=1
        for i in range(k,rows):
            layer.append(locker[i][cols-1])
            position[index]=[i,cols-1]
            index+=1
        cols-=1
        if k<rows:
            i=cols-1
            while(i>=l):
                layer.append(locker[rows-1][i])
                position[index]=[rows-1,i]
                index+=1
                i-=1
            rows-=1
        if l<cols:
            i=rows-1
            while(i>=k):
                layer.append(locker[i][l])
                position[index]=[i,l]
                index+=1
                i-=1
            l+=1
        size=len(layer)
        if size==0:
            return
        r=rotate[layer_number]
        r=r%size
        for i in range(size):
            dirtn=i
            if layer_number%2:
                dirtn=dirtn-r
            else:
                dirtn=dirtn+r
            dirtn=dirtn+size
            dirtn=dirtn %size
            dirtn=dirtn +size
            dirtn=dirtn%size
            locker[position[dirtn][0]][position[dirtn][1]]=layer[i]
        layer_number+=1

rows,cols=map(int,input().split())
locker=[]
for i in range(rows):
    locker.append(list(map(int,input().split())))
rotate=list(map(int,input().split()))
rotate.insert(0,0)
solve_unlock(locker,rotate,rows,cols)
for row in range(rows):
    for col in range(cols):
        print(locker[row][col], end=" ")
        if col==cols:
            continue
    if row==rows:
        continue
    print()
#input
'''
4 4
1 2 3 4
2 3 4 5
2 4 5 6
2 3 4 5
2 2
'''
