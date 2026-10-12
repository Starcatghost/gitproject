import requests 
def get_all_item():
    url = 'http://127.0.0.1:8000/getItems/'
    response = requests.get(url)
    if response.status_code != 200:
       return 'ERROR'
    else:
        response = response.json
        return response

if __name__=='__main__':
    result = get_all_item()
    print('result: ', result)    