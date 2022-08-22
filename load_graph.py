# Author: Ivy Zhang
# Date: 03/04/2022


from vertex import Vertex


def load_graph(filename):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:
        section_split = l.split(";")
        vertex_name = section_split[0].strip()
        x_coordinate = section_split[2].split(",")[0].strip()
        y_coordinate = section_split[2].split(",")[1].strip()
        vertex = Vertex(vertex_name, x_coordinate, y_coordinate)
        vertex_dict[vertex.name] = vertex  # putting vertex at the key of its name

    file.close()
    file = open(filename, "r")
    for l in file:
        section_split = l.split(";")
        adjacent_vertices = section_split[1].split(",")
        current_vertex = vertex_dict[section_split[0].strip()]
        for v in adjacent_vertices:
            vertex_item = vertex_dict[v.strip()]
            current_vertex.adj_list.append(vertex_item)

    file.close()
    return vertex_dict

vertex_dict = load_graph("dartmouth_graph.txt")
out_file = open("vertices.txt", "w")
for vertex in vertex_dict:
    out_file.write(str(vertex_dict[vertex]) + "\n")
out_file.close()
