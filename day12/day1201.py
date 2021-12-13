def main(f):
    with open(f, "r") as file1:
        lines = [(line.strip()).split('|') for line in file1 if line.strip()]

    print(part1(lines))

def part1(lines):

    graph = {}
    
    for l in range(len(lines)):
        teststring = str(lines[l])
        sleutel = teststring[2 : int(teststring.index('-'))]
        waarde = teststring[int(teststring.index('-')) + 1 : len(teststring) - 2]
        graph.setdefault(sleutel, list()).append(waarde)
        graph.setdefault(waarde, list()).append(sleutel)

    print(find_all_paths(graph, "start", "end"))    
    
    return graph

def find_all_paths(graph, start_vertex, end_vertex, path=[]):
    """ find all paths from start_vertex to 
        end_vertex in graph """
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = find_all_paths(graph, vertex, end_vertex, path)
            for p in extended_paths: 
                paths.append(p)
    return paths

def part2(lines):
    finalscore = 0

    return finalscore

if __name__ == "__main__":
    main('test.txt')