#! python3
class Tracker:  # or just T is a tracker class to track data changes more efficiently/visually than globals????????
    pass


def q(x):  # so that I don't have to type ...."[Q%d]" % x.... forever
    return "[Q%d]" % x


def is_crossing_and_attacked(pos, list_of_coords):  # check whether my pos is attacked by other's...
    for (x, y) in list_of_coords.values():  # for checking and getting positions of each queen
        try:
            slope = (pos[1] - y) / (pos[0] - x)
            if (slope == 0) or (slope == 1) or (slope == -1):  # lil maths for ya
                return True
        except ZeroDivisionError:
            return True
    else:
        return False


def increase_y_i_mean_row_by_one():
    T.y += 1


def go_to_previous_column_or_maybe_one_column_back():
    T.x -= 1


def go_to_next_column_i_mean_increase_x_by_one():
    T.x += 1


def start_from_first_row():
    T.y = 0


def set_y_to_that_of_queen_no(x):
    T.y = T.coord_dict[q(x)][1]


def solution_is_unique():
    current_list_of_solution = []
    for x, y in T.coord_dict.values():
        current_list_of_solution.append(y)
    if current_list_of_solution in T.unique_list:
        return
    else:
        T.unique_list.append(current_list_of_solution)
        return True


def solution_is_valid():
    for x, y in T.coord_dict.values():
        T.set.add(y)

    if T.set == T.sample_set: return True


def set_y_as_required():
    if T.x == 0:
        return "break the loop"
    else:
        set_y_to_that_of_queen_no(T.x)
        del T.coord_dict[q(T.x)]
    if T.y == T.grid_length:
        go_to_previous_column_or_maybe_one_column_back()
        set_y_as_required()


def logic_queens_mainloop():
    while T.x <= T.grid_length:  # of course, I mean why would you loop after that dict has all queens queens already?
        T.pos = [T.x, T.y]  # new point of consideration might be the new (x and y)'s obviously???
        if is_crossing_and_attacked(T.pos, T.coord_dict):  # check if curr_position is crossing.....
            # ............................................... and attacked by any other queens......
            if T.y < T.grid_length:  # attacked by queens but can move below to check other positions. Of course...
                # .....................grid hasn't ended yet because queens position is above the last grid........
                pass
            elif T.y == T.grid_length:  # attacked by queen but can't move any below, I mean can you go below the grid?
                go_to_previous_column_or_maybe_one_column_back()
                what_to_do = set_y_as_required()
                if what_to_do == "break the loop": break

        else:
            T.coord_dict[q(T.x)] = T.pos
            go_to_next_column_i_mean_increase_x_by_one()
            start_from_first_row()
            r"so that we can start checking from the very top of the column" \
             "don't worry T.y +=1 just below will set T.y = 1 "

        if T.y < T.grid_length:  # I mean can you go further below than last grid?, could you?
            T.y += 1  # so that y always increases or let's say-queen searches the next position....
    print_if_unique()  # you know what print the solution, if loop has broken, because, it found solution....
    if T.x != 0:
        logic_queens_mainloop()


def find_next_solution_if_exists(queen_number):
    set_y_to_that_of_queen_no(queen_number)
    del T.coord_dict[q(queen_number)]
    if T.y == T.grid_length:
        find_next_solution_if_exists((queen_number := queen_number - 1))
    increase_y_i_mean_row_by_one()
    T.x = queen_number


def print_if_unique():
    if T.x == 0:
        print("There're", T.count, "solutions.")
    elif solution_is_valid() and solution_is_unique():
        virtual_print(T.coord_dict)
        find_next_solution_if_exists(T.grid_length)
        '" in case we want to find all solutions I\'d have to move the cursor"\
        "of the last queen below than it already is or move backwards if no places are"\
         "left, which is done by our good old while loop'


def create_empty_list():  # just for creation of sth important jk, it's a
    # list of list of list_strings with grid*grid dimensions
    inner_list = ['[  ]'] * T.grid_length
    outer_list = [inner_list[:] for i in range(T.grid_length)]
    coord_list = outer_list[:]
    return coord_list


def virtual_print(new_solution):  # just print the formatted form of queens from the supplied dict of new solutions
    coord_list = create_empty_list()
    T.count += 1
    for key, data in new_solution.items():
        coord_list[data[1] - 1][data[0] - 1] = key
    picture = ""
    for string_list in coord_list:
        picture += add(string_list)
    print(picture)


def add(list_of_strings):  # just to get the first row of the matrix... as string from the list supplied
    return "".join(list_of_strings) + "\n"  # joins the list with delimiter("")


T = Tracker
T.x = 1  # my initial x_coord
T.y = 1  # my initial y_coord
T.count = 0  # counter to count how many ways can we
T.coord_dict = {}  # initialization of dict that contains queens and their subsequent coord...
T.queen_counter = 0
T.grid_length = int(input("Enter no.of grids?: "))
T.unique_list = []
T.sample_set = {x for x in range(1, T.grid_length + 1)}
T.set = set()

if __name__ == "__main__":
    import time

    a = time.time()
    logic_queens_mainloop()  # start the game
    b = time.time()
    print("This is the solution set,\n....................."
          "\n..............................................\n" )
    for i in T.unique_list:
        print(i)
    print(".........................\n.....................")
    print(b - a, "seconds taken.")
    input()

from tkinter import *
from tkinter.scrolledtext import ScrolledText

















