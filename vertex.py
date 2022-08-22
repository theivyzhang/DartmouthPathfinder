# Author: Ivy Zhang
# Date: 03/04/2022

from cs1lib import *

VERTEX_RADIUS = 15


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.adj_list = []
        self.x = int(x)
        self.y = int(y)

    # function that draws the vertices
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # function that draws the edges
    def draw_edge(self, adj_vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(7)
        draw_line(self.x, self.y, adj_vertex.x, adj_vertex.y)

    # function that creates the paths for the entire map
    def full_map_edges(self, r, g, b):
        for vertex in self.adj_list:
            self.draw_edge(vertex, r, g, b)

    # smallest surrounding square function
    def s_s_square(self, x, y):
        return (self.x - VERTEX_RADIUS / 2 < x < self.x + VERTEX_RADIUS / 2) \
               and (self.y - VERTEX_RADIUS / 2 < y < self.y + VERTEX_RADIUS / 2)

    # function for the string output
    def __str__(self):
        string = ""
        for index in range(len(self.adj_list)):
            string = string + str(self.adj_list[index].name) + ", "
        helper = len(self.adj_list) - 1
        string = string + str(self.adj_list[helper].name)
        return str(self.name) + "; " + "Location: " + str(self.x) + ", " + str(
            self.y) + "; " + "Adjacent vertices: " + string
