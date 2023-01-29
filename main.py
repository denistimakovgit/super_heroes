import requests

def smartest_hero():
    """
    Функция определения самого умного(intelligence) из трех
    супергероев - Hulk, Captain America, Thanos.
    """

    url = "https://akabab.github.io/superhero-api/api//all.json"
    responce = requests.get(url=url)
    heroes = responce.json()
    heroes_names = ['Hulk', 'Captain America', 'Thanos']
    three_heroes = {}

    for elem in heroes:
        if elem['name'] in heroes_names:
            print(elem['name'])
            print(elem['powerstats']['intelligence'])
            three_heroes[elem['name']] = elem['powerstats']['intelligence']

    sorted_heroes = {k: v for k, v in sorted(three_heroes.items(), key=lambda item: item[1])}
    print(f'Самый умный супер-герой: {list(sorted_heroes.keys())[-1]}')

if __name__ == '__main__':
    smartest_hero()


