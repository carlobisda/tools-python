#Name: Randum Level Generator
#Author: Carlo Bisda
#License: MIT
#Version: 1.0.0

import random

#DEFINE CONSTANTS FOR THE DUNGEON AND ROOM SIZE
DUNGEON_WIDTH=60
DUNGEON_HEIGHT=30
ROOM_MIN_SIZE=5
ROOM_MAX_SIZE=10

#INIT DUNGEON ARRAY WITH WALLS
dungeon=[[1 for y in range(DUNGEON_HEIGHT)] for x in range(DUNGEON_WIDTH)]

#FUNCTION TO CREATE ROOM IN THE DUNGEON
def create_room(x, y, w, h):
    for i in range(x, x+w):
        for j in range(y, y+h):
            dungeon[i][j]=0

#FUNCTION TO CREATE A HORIZONTAL TUNNEL IN DUNGEON
def create_h_tunnel(x1, x2, y):
    for i in range(min(x1, x2), max(x1, x2)+1):
        dungeon[i][y]=0

#FUNCTION TO CREATE VERTICAL TUNNEL IN DUNGEON
def create_v_tunnel(y1, y2, x):
    for i in range(min(y1, y2), max(y1, y2)+1):
        dungeon[x][i]=0

#FUNCTION TO GENERATE DUNGEON
def generate_dungeon(num_rooms):
    rooms=[]
    for i in range(num_rooms):
        #GENERATE RANDOM WIDTH AND HEIGHT FOR ROOM
        w=random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h=random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        #GENERATE RANDOM POSITION FOR ROOMS IN DUNGEON
        x=random.randint(0, DUNGEON_WIDTH-w-1)
        y=random.randint(0, DUNGEON_HEIGHT-h-1)
        #CREATE ROOM IN DUNGEON
        create_room(x, y, w, h)
        if i==0:
            #IF FIRST ROOM GENERATED, CREATE A TUNNEL TO NEXT ROOM
            prev_x=x
            prev_y=y
        else:
            #IF NOT FIRST ROOM, CREATE TUNNEL TO PREVIOUS ROOM
            new_x=x+int(w/2)
            new_y=y+int(h/2)
            create_h_tunnel(prev_x, new_x, prev_y)
            create_v_tunnel(prev_y, new_y, new_x)
            prev_x=new_x
            prev_y=new_y
        rooms.append((x, y, w, h))
    return rooms

#GENERATE A 10 ROOM DUNGEON
rooms=generate_dungeon(10)

#PRINT DUNGEON IN TERMINAL
for y in range(DUNGEON_HEIGHT):
    for x in range(DUNGEON_WIDTH):
        if dungeon[x][y]==1:
            print("=", end="")
        else:
            print(":", end="")
    print()