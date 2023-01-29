import requests
import json

def get_search(params, keyword):
    url_params = {
        'applicationId' : params['rakuten_application_id'],
        'keyword' : keyword,
        'page' : params['page'],
        'hits' : params['hits'],
    }
    response = requests.get(params['base_url'], url_params)
    text = json.loads(response.text)
    
    items_params_list = []
    for item in text['Items']:
        item_params_dict = {}
        item_params_dict['item_name'] = item['Item']['itemName']
        item_params_dict['item_price'] = item['Item']['itemPrice']
        item_params_dict['item_url'] = item['Item']['itemUrl']
        item_params_dict['catchcopy'] = item['Item']['catchcopy']
        item_params_dict['thumbnail_url'] = item['Item']['mediumImageUrls'][0]['imageUrl']
        item_params_dict['review_count'] = item['Item']['reviewCount']
        item_params_dict['review_average'] = item['Item']['reviewAverage']
        item_params_dict['review_rating'] = item_params_dict['review_average']/5 * 100
        item_params_dict['point_rate'] = item['Item']['pointRate']
        item_params_dict['shop_name'] = item['Item']['shopName']
        item_params_dict['shop_url'] = item['Item']['shopUrl']

        items_params_list.append(item_params_dict)

    return items_params_list