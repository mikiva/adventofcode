data_input = 347991




order = ["RU", "LD"]
direction = dict(R=(1,0), U=(0,-1), L=(-1, 0), D=(0, 1))


current_pos = (0,0)

grid=[current_pos]


def move(pos, vec):
    new_pos = pos
    new_pos = new_pos[0] + vec[0], new_pos[1] + vec[1]

    return new_pos



for i in range(1000):
    moves = list(order[i%2])
    
    for movement in range(i):
        vector = direction.get(moves[0])
        current_pos = move(current_pos, vector)
        grid.append(current_pos)
    for movement in range(i):
        vector = direction.get(moves[1])
        current_pos = move(current_pos, vector)
        grid.append(current_pos)


    

def manhattan_distance(outer_position):
    x1, y1 = 0, 0

    x2, y2 =  outer_position[0], outer_position[1]

    distance = abs(x1 - x2)  + abs(y1- y2) 
    return distance


print("p1", manhattan_distance(grid[data_input-1])) 

