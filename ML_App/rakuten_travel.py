import requests
import json

def get_search(params, keyword):
    url_params = {
        'applicationId' : params['rakuten_application_id'],
        'keyword' : keyword,
        'page' : params['page'],
        'hits' : params['hits'],
        'hotelThumbnailSize' : params['hotel_thumbnail_size'],
        'responseType' : params['response_type'],
    }
    response = requests.get(params['base_url'], url_params)
    text = json.loads(response.text)
    

    hotels_params_list = []
    for hotel in text['hotels']:
        hotel_params_dict = {}
        hotel_params_dict['hotel_name'] = hotel['hotel'][0]['hotelBasicInfo']['hotelName']
        hotel_params_dict['hotel_info_url'] = hotel['hotel'][0]['hotelBasicInfo']['hotelInformationUrl']
        hotel_params_dict['review_url'] = hotel['hotel'][0]['hotelBasicInfo']['reviewUrl']
        hotel_params_dict['review_count'] = hotel['hotel'][0]['hotelBasicInfo']['reviewCount']
        hotel_params_dict['review_average'] = hotel['hotel'][0]['hotelBasicInfo']['reviewAverage']
        hotel_params_dict['hotel_min_charge'] = hotel['hotel'][0]['hotelBasicInfo']['hotelMinCharge']
        hotel_params_dict['hotel_special'] = hotel['hotel'][0]['hotelBasicInfo']['hotelSpecial']
        hotel_params_dict['hotel_thumbnail_url'] = hotel['hotel'][0]['hotelBasicInfo']['hotelThumbnailUrl']

        if hotel_params_dict['review_average'] is None:
            hotel_params_dict['review_average'] = 0
        hotel_params_dict['review_rating'] = hotel_params_dict['review_average']/5 * 100
        
        hotel_params_dict['area_name'] = hotel['hotel'][2]['hotelDetailInfo']['areaName']
        
        hotel_params_dict['hotel_other_info'] = hotel['hotel'][5]['hotelOtherInfo']['otherInformation']

        hotels_params_list.append(hotel_params_dict)

    return hotels_params_list