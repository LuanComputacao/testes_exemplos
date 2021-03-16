from requests import request


class RickAndMortyImage:
    def __init__(self):
        self.url = 'https://rickandmortyapi.com/api/character'

    def get_images(self):
        response = request('GET', self.url).json()['results']
        # print(type{reponse})

        # ipdb.set_trace()

        return [char['image'] for char in response]
