import requests
import json

def get_search(params, keyword):
    url_params = {
        'key' : params['api_key'],
        'keyword' : keyword,
        'format' : 'json',
        'count' : 20,
    }
    response = requests.get(params['base_url'], url_params)
    text = json.loads(response.text)

    shops_params_list = []
    for shop in text['results']['shop']:
        shop_params_dict = {}
        shop_params_dict['name'] = shop['name']
        shop_params_dict['address'] = shop['address']
        shop_params_dict['station_name'] = shop['station_name']
        shop_params_dict['genre_name'] = shop['genre']['name']
        shop_params_dict['catch'] = shop['catch']
        shop_params_dict['access'] = shop['access']
        shop_params_dict['site_url'] = shop['urls']['pc']
        shop_params_dict['photo_url'] = shop['photo']['pc']['l']
        shop_params_dict['open'] = shop['open']
        shop_params_dict['close'] = shop['close']
        shop_params_dict['budget'] = shop['budget']['average']
        
        shops_params_list.append(shop_params_dict)

    return shops_params_list