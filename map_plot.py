# Author: Ivy Zhang
# Date: 03/06/2022

from cs1lib import *
from load_graph import *
from bfs import breadth_first_search

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
start_vertex = None
goal_vertex = None
mpressed = False
x = 0
y = 0


# the function that controls what happens when I press my mouse/trackpad
def press_mouse(mx, my):
    global x, y, mpressed
    x = mx  # passing in mouse is initialized
    y = my
    mpressed = True


# the function that controls when my mouse moves
def move_mouse(mx, my):
    global x, y
    x = mx
    y = my


# the function that controls what happens when I release my mouse/trackpad
def release_mouse(mx, my):
    global mpressed
    mpressed = False


# dartmouth map background
def background():
    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)


# map main canvas
def map_canvas():
    global x, y, mpressed, start_vertex, goal_vertex
    background()

    for key in vertex_dict:
        vertex_dict[key].draw_vertex(0, 0, 1)
        vertex_dict[key].full_map_edges(0, 0, 1)

    if mpressed:  # if we press mouse, we want to initialize start vertex at this point
        for key in vertex_dict:
            if vertex_dict[key].s_s_square(x, y):
                start_vertex = vertex_dict[key]

    for key in vertex_dict:  # check if we are at end vertex
        if vertex_dict[key].s_s_square(x, y):
            goal_vertex = vertex_dict[key]

    if start_vertex != None and goal_vertex != None:
        list = breadth_first_search(start_vertex, goal_vertex)
        start_vertex.draw_vertex(1, 0, 0)
        for i in range(len(list) - 1):
            list[i].draw_vertex(1, 0, 0)
            list[i].draw_edge(list[i + 1], 1, 0, 0)


start_graphics(map_canvas, mouse_press=press_mouse, mouse_release=release_mouse, mouse_move=move_mouse,
               width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
