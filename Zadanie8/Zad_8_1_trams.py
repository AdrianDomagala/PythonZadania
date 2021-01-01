import json
import random
import time
from statistics import mean


class Stops_graph:
    INFINITY = 9999
    NUM_OF_SEARCH = 5000
    WEIGHT = 1

    def __init__(self, file_name):
        self.graph = {}
        self.__get_stops_from_file(file_name)
        self.all_edges = []
        self.__get_all_edge()

    def __get_stops_from_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as read_file:
            data = json.load(read_file)
        for tram in data['tramwaje']:
            last_stop = tram['tprzystanki'][0]['name']
            for i, n in enumerate(tram['tprzystanki'][1:]):
                current_stop = n['name']
                stops_curr = self.graph.get(current_stop, set())
                stops_curr.add(last_stop)
                self.graph[current_stop] = stops_curr

                stops_last = self.graph.get(last_stop, set())
                stops_last.add(current_stop)
                self.graph[last_stop] = stops_last
                last_stop = current_stop

    def __get_all_edge(self):
        for vertex, edges in self.graph.items():
            for e in edges:
                self.all_edges.append([vertex, e])
        return self.all_edges

    def random_stops(self):
        random_stops = []
        for i in range(0, self.NUM_OF_SEARCH):
            random_stops.append(random.sample(self.graph.keys(), 2))
        return random_stops

    def __stop_with_minimal_cost(self, stops_possible_to_visit, costs_of_visit, end):
        min = costs_of_visit.get(end, self.INFINITY) if end in stops_possible_to_visit else self.INFINITY
        name = end
        for stop in stops_possible_to_visit:
            if min > costs_of_visit[stop]:
                min = costs_of_visit[stop]
                name = stop
        stops_possible_to_visit.remove(name)
        return name

    def dijkstra(self, start, end):
        stops_possible_to_visit = set()
        costs_of_visit = {}

        for stop in self.graph[start]:
            costs_of_visit[stop] = self.WEIGHT
            stops_possible_to_visit.add(stop)

        while True:
            current_stop = self.__stop_with_minimal_cost(stops_possible_to_visit, costs_of_visit, end)
            if current_stop == end:
                return costs_of_visit[end]

            for stop in self.graph[current_stop]:
                cost = costs_of_visit.get(stop, self.INFINITY)
                if cost > costs_of_visit[current_stop] + self.WEIGHT:
                    costs_of_visit[stop] = costs_of_visit[current_stop] + self.WEIGHT
                    stops_possible_to_visit.add(stop)

    def bellman_ford(self, start, end):
        costs_of_visit = {start: 0}
        for i in range(0, len(self.all_edges) - 1):
            changed = False
            for v_from, v_to in self.all_edges:
                from_cost = costs_of_visit.get(v_from, self.INFINITY)
                to_cost = costs_of_visit.get(v_to, self.INFINITY)
                if to_cost > from_cost + self.WEIGHT:
                    costs_of_visit[v_to] = from_cost + self.WEIGHT
                    changed = True
            if not changed:
                return costs_of_visit[end]
        return costs_of_visit[end]

    def floyd_warshall(self, starts_and_ends):
        shortest_paths_matrix = self.__floyd_warshall_matrix()
        shortest_paths = []
        for stops in starts_and_ends:
            shortest_paths.append(shortest_paths_matrix[stops[0]][stops[1]])
        return shortest_paths

    def __floyd_warshall_matrix(self):
        shortest_paths_matrix = self.__floyd_warshall_initial_matrix()
        for stop_between in self.graph.keys():
            for stop_from in self.graph.keys():
                for stop_to in self.graph.keys():
                    shortest_paths_matrix[stop_from][stop_to] = min(
                        shortest_paths_matrix[stop_from].get(stop_to, self.INFINITY),
                        shortest_paths_matrix[stop_from].get(stop_between, self.INFINITY) +
                        shortest_paths_matrix[stop_between].get(stop_to, self.INFINITY)
                    )
        return shortest_paths_matrix

    def __floyd_warshall_initial_matrix(self):
        shortest_paths_matrix = {}
        for stop_from in self.graph.keys():
            for stop_to in self.graph[stop_from]:
                edges = shortest_paths_matrix.get(stop_from, {})
                edges[stop_to] = self.WEIGHT
                shortest_paths_matrix[stop_from] = edges
        return shortest_paths_matrix


stops_graph = Stops_graph('src/tramwaje.json')
random_stops = stops_graph.random_stops()

dijkstra_results = []
td0 = time.time()
for stops in random_stops:
    dijkstra_results.append(stops_graph.dijkstra(stops[0], stops[1]))
td1 = time.time()
print("Dijkstra time: ", td1 - td0)
print("mean: ", mean(dijkstra_results))

bellman_ford_results = []
tbf0 = time.time()
for stops in random_stops:
    bellman_ford_results.append(stops_graph.bellman_ford(stops[0], stops[1]))
tbf1 = time.time()
print("Bellman-Ford time: ", tbf1 - tbf0)
print("mean: ", mean(bellman_ford_results))

tfw0 = time.time()
floyd_warshall_results = stops_graph.floyd_warshall(random_stops)
tfw1 = time.time()
print("Floyd-Warshall time: ", tfw1 - tfw0)
print("mean: ", mean(floyd_warshall_results))

# print(stops_graph.dijkstra('Wzgórza Krzesławickie', 'Darwina'))
# print(stops_graph.dijkstra('Teatr Słowackiego', 'Biprostal'))
# print(stops_graph.dijkstra('Biprostal', 'Kampus UJ'))
#
# print(stops_graph.bellman_ford('Wzgórza Krzesławickie', 'Darwina'))
# print(stops_graph.bellman_ford('Teatr Słowackiego', 'Biprostal'))
# print(stops_graph.bellman_ford('Biprostal', 'Kampus UJ'))
#
# print(stops_graph.floyd_warshall([['Wzgórza Krzesławickie', 'Darwina'],
#                                   ['Teatr Słowackiego', 'Biprostal'],
#                                   ['Biprostal', 'Kampus UJ']]))
