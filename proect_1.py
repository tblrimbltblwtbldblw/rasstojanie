from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480)
}

distance = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distance['Moscow'] = {}
distance['Moscow']['London'] = moscow_london
distance['Moscow']['Paris'] = moscow_paris
distance['London'] = {}
distance['London']['Paris'] = london_paris

pprint(distance)
