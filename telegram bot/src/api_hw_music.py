import requests


def get_song_info_by_name(song_name):
    url = f'https://openwhyd.org/hot/electro?format=json'
    params_dict = {'q': song_name }
    response = requests.get(url, params=params_dict)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        result = response['tracks'][0]
        name = result['name']
        trackUrl = result['trackUrl']

        return (name,trackUrl)




if __name__ == '__main__':
    song_name = input('enter song name: ')
    result = get_song_info_by_name(song_name)
    print(f'result: {result}')




def get_music(music_name):

    url = 'https://openwhyd.org/hot/electro?format=json'
    response = requests.get(url)

    if response.status_code != 200:
        return 'ERROR'
    response = response.json()

    for music in response['tracks']:
        if music_name.lower() in music['name'].lower():
            return music['name'], music['trackUrl']

    return music


if __name__ == '__main__':
    music_name = input('Enter music name: ')
    result = get_music(music_name)
    print(result)
