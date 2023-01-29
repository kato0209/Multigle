import requests
import json
import datetime
import dateutil.parser

def get_search(access_token, keyword):
    per_page = 10
    page = 1

    url = (
        f"https://qiita.com/api/v2/items?page={page}&per_page={per_page}&"
        f"query=body:{keyword}"
    )
    headers = {"Authorization" : f"Bearer {access_token}"}
    response = requests.get(url, headers = headers,timeout=3.0)
    text = json.loads(response.text)

    response_dicts = []
    for value in text:
        response_dict = {}
        response_dict['id'] = value['user']['id']
        response_dict['likes_count'] = value['likes_count']

        created_at = value['created_at']
        JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
        jst_datetime = dateutil.parser.parse(created_at).astimezone(JST)
        created_at = jst_datetime.date().strftime(('%Y年%m月%d日'))
        response_dict['created_at'] = created_at


        tag_list = []
        for tag in value['tags']:
            tag_list.append(tag['name'])
        response_dict['tags'] = tag_list
        
        response_dict['profile_image_url'] = value['user']['profile_image_url']
        response_dict['url'] = value['url']
        response_dict['title'] = value['title']
        response_dict['body'] = value['body']
        response_dicts.append(response_dict)
        
    return response_dicts
