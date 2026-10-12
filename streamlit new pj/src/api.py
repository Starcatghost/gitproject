import requests

def get_movie1_list_by_page(page=1):
    url = "https://moviesapi.ir/api/v1/movies"

    api_paragms = {'page': page}
    response = requests.get(url, params= api_paragms)

    if response.status_code != 200:
        return 'ERROR'

    else:
        response = response.json()

        return response

if __name__ == '__main__':
    result = get_movie1_list_by_page()
    print(result)