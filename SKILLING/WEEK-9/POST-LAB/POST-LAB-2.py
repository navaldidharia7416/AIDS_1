# Alex and newt are playing a game with n stones where Alex always plays first. The two
# players move in alternating turns and plays optimally. In a single move a player can remove
# either 1, 3 or 4 stones from the pile of stones. If a player is unable to make a move, then that
# player loses the game. Given the number of stones where n is less than equal to 200, find and
# print the name of the winner.
# MAX = 200


# finds the winning and losing
# states for the 200 stones.
def findStates(position):
    # 0 means losing state
    # 1 means winning state
    position[0] = 0;
    position[1] = 1;
    position[2] = 0;
    position[3] = 1;
    position[4] = 1;
    position[5] = 1;
    position[6] = 1;
    position[7] = 0

    # find states for other positions
    for i in range(8, max + 1):
        if not (position[i - 1]) or not (position[i - 3]) or not (position[i - 4]):
            position[i] = 1;
        else:
            position[i] = 0;


# driver function
N = 100
position = [0] * (max + 1)

findStates(position)

if (position[N] == 1):
    print("Player 1")
else:
    print("Player 2")

# This code is contributed by
# Smitha Dinesh Semwal
