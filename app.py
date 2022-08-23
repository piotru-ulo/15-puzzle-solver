from asyncio.windows_events import NULL
from flask import Flask, render_template
import json
import copy

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('15.html')

graph  = [ [] ,
    [2, 5] , [1, 3, 6] , [2, 4, 7], [3, 8],
    [1, 6, 9], [2, 5, 7, 10], [3, 6, 8, 11], [4, 7, 12],
    [5, 10, 13], [6, 9, 11, 14], [7, 10, 12, 15], [8, 11, 16],
    [9, 14], [10, 13, 15], [11, 14, 16], [12, 15]
]


@app.route('/solve/<input>')
def solve(input):
    array = json.loads(input)

    # first line
    moves = s1(array, 1, 1) + s1(array, 2, 2) + s1(array, 3, 3) + s1(array, 4, 12)
    if(array[4] != 4):
        start = 0
        for i in range(1, 17):
            if array[i] == None:
                start = i
        tmparr = bfs(start, 7, 4, array)
        swap(array, tmparr + [7, 3, 4, 8, 7, 3, 4, 8, 12, 11, 7, 3, 4, 8])
        moves += tmparr + [7, 3, 4, 8, 7, 3, 4, 8, 12, 11, 7, 3, 4, 8]

    # second line
    moves += s1(array, 5, 5) + s1(array, 6, 6) + s1(array, 7, 7) + s1(array, 8, 16)
    if(array[8] != 8):
        start = 0
        for i in range(1, 17):
            if array[i] == None:
                start = i
        tmparr = bfs(start, 11, 8, array)
        swap(array, tmparr + [11, 7, 8, 12, 11, 7, 8, 12, 16, 15, 11, 7, 8, 12])
        moves += tmparr + [11, 7, 8, 12, 11, 7, 8, 12, 16, 15, 11, 7, 8, 12]
    
    # 9 and 13
    moves += s1(array, 9, 9) + s1(array, 13, 15)
    if(array[13] != 13):
        for i in range(1, 17):
            if array[i] == None:
                start = i
        tmparr = bfs(start, 10, 13, array)
        swap(array, tmparr + [9, 13, 14, 10, 9, 13, 14, 15, 11, 10, 9, 13, 14])
        moves += tmparr + [9, 13, 14, 10, 9, 13, 14, 15, 11, 10, 9, 13, 14]
    
    # 10 and 14
    moves += s1(array, 10, 10) + s1(array, 14, 16)
    if(array[14] != 14):
        for i in range(1, 17):
            if array[i] == None:
                start = i
        tmparr = bfs(start, 11, 14, array)
        swap(array, tmparr + [10, 14, 15, 11, 10, 14, 15, 16, 12, 11, 10, 14, 15])
        moves += tmparr + [10, 14, 15, 11, 10, 14, 15, 16, 12, 11, 10, 14, 15]
    
    # 11, 12 and 15
    moves += s1(array, 11, 11)
    if(array[12] != 12):
        moves +=[12, 16]
        swap(array, [12, 16])
    if(array[15] != 15):
        moves +=[15, 16]
        swap(array, [15, 16])
    

    
    myJSON = json.dumps(moves)

    return (myJSON)

def bfs(start, end, limit, array):
    queue = [[start, [start]]]
    vis = [start]
    l2 = limit
    if(limit == 13 or limit == 14):
        limit -= 4

    if(start == end):
        return [start]
    while(True):
        front = queue.pop(0)
        for i in graph[front[0]]:
            if i not in vis and array[i] > limit and array[i]!=l2: 
                vis.append(i)
                f2 = copy.deepcopy(front)
                f2[1].append(i)
                f2[0] = i
                queue.append(copy.deepcopy(f2))
                if i == end:
                    return f2[1]

# simple move tile to goal
def s1(array, tile, goal):
    moves = []
    place = 0
    for i in range(1, 17):
        if array[i] == tile:
            place = i
    # 4 and 8 exceptions
    if(tile == 4 or tile == 8):
        if(array[tile] == tile):
            return []
        if(array[tile] == None and array[tile + 4] == tile):
            swap(array, [tile, tile + 4])
            return [tile, tile + 4]
    
    # 13 and 14 exceptions
    if(tile == 13 or tile == 14):
        if(array[tile] == tile):
            return []
        if(array[tile] == None and array[tile + 1] == tile):
            swap(array, [tile, tile + 1])
            return [tile, tile + 1]



    # - left, + right
    lr = ((goal-1) % 4) - ((place-1)%4)
    up = ((place-1)//4) - ((goal-1)//4)
    
    # horizontal movement
    while(lr !=0 ):
        start = 0
        end = place
        tmp = [end]
        if(lr<0):
            place -= 1
            end -= 1
            for i in range(1, 17):
                if array[i] == None:
                    start = i
            lr = lr + 1
        
        else:
            end += 1
            place += 1
            for i in range(1, 17):
                if array[i] == None:
                    start = i
            lr = lr - 1

        tmp = bfs(start, end, tile, array) + tmp
        moves = moves + copy.deepcopy(tmp)
        swap(array, tmp)
    
    # vertica movement
    while(up!=0):
        end = place
        start = 0
        tmp = [end]
        if(up>0):
            end -= 4
            place -= 4
            up -= 1
        else:
            end +=4
            place +=4
            up +=1
        for i in range(1, 17):
            if array[i] == None:
                start = i
        
        tmp = bfs(start, end, tile, array) + tmp
        moves = moves + copy.deepcopy(tmp)
        swap(array, tmp)
    return moves

# swap tiles in array
def swap(array, tmp):
    for i in range(1, len(tmp)):
        array[tmp[i-1]] = array[tmp[i]]
        array[tmp[i]] = None
    return 


