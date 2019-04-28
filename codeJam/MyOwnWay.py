tests = int(input())


def move(position, mv):
    x, y = position
    if mv == "e":
        return x + 1, y
    elif mv == "s":
        return x, y + 1
    return position


def undo_move(position, mv):
    x, y = position
    if mv == "e":
        return x - 1, y
    elif mv == "s":
        return x, y - 1


def rewind(position, path):
    r_pos = undo_move(position, path.pop())
    return r_pos, path


def other_move(mv):
    if mv == "s":
        return "e"
    elif mv == "e":
        return "s"


def my_move(position, maze_size):
    x, y = position
    if x < maze_size:
        return "e"
    elif y < maze_size:
        return "s"


def outside_maze(position, maze_size):
    x, y = position
    return x > maze_size or y > maze_size


for i in range(tests):
    n = int(input())
    ll_path = list(str(input()).lower())
    ll_pos = (1, 1)
    my_pos = (1, 1)
    my_path = []
    for ll_nxt_mv in ll_path:
        my_nxt_mv = other_move(ll_nxt_mv)
        my_path.append(my_nxt_mv)
        my_pos = move(my_pos, my_nxt_mv)
        ll_pos = move(ll_pos, ll_nxt_mv)
    print("Case #" + str(i + 1) + ": " + "".join(my_path).upper())
