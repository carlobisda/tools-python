import random

# Define constants for the dungeon size and room size
DUNGEON_WIDTH = 60
DUNGEON_HEIGHT = 30
ROOM_MIN_SIZE = 5
ROOM_MAX_SIZE = 10

# Initialize the dungeon array with walls
dungeon = [[1 for y in range(DUNGEON_HEIGHT)] for x in range(DUNGEON_WIDTH)]

# Define a function to create a room in the dungeon
def create_room(x, y, w, h):
    for i in range(x, x + w):
        for j in range(y, y + h):
            dungeon[i][j] = 0

# Define a function to create a horizontal tunnel in the dungeon
def create_h_tunnel(x1, x2, y):
    for i in range(min(x1, x2), max(x1, x2) + 1):
        dungeon[i][y] = 0

# Define a function to create a vertical tunnel in the dungeon
def create_v_tunnel(y1, y2, x):
    for i in range(min(y1, y2), max(y1, y2) + 1):
        dungeon[x][i] = 0

# Define a function to generate the dungeon
def generate_dungeon(num_rooms):
    rooms = []
    for i in range(num_rooms):
        # Generate a random width and height for the room
        w = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        h = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
        # Generate a random position for the room within the dungeon
        x = random.randint(0, DUNGEON_WIDTH - w - 1)
        y = random.randint(0, DUNGEON_HEIGHT - h - 1)
        # Create the room in the dungeon
        create_room(x, y, w, h)
        if i == 0:
            # If this is the first room, create a tunnel to the next room
            prev_x = x
            prev_y = y
        else:
            # If this is not the first room, create a tunnel to the previous room
            new_x = x + int(w/2)
            new_y = y + int(h/2)
            create_h_tunnel(prev_x, new_x, prev_y)
            create_v_tunnel(prev_y, new_y, new_x)
            prev_x = new_x
            prev_y = new_y
        rooms.append((x, y, w, h))
    return rooms

# Generate a dungeon with 10 rooms
rooms = generate_dungeon(10)

# Print out the dungeon
for y in range(DUNGEON_HEIGHT):
    for x in range(DUNGEON_WIDTH):
        if dungeon[x][y] == 1:
            print("#", end="")
        else:
            print(".", end="")
    print()
