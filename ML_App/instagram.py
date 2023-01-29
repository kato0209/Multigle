import requests
import json
import os
from . import models


def get_search(params, keyword):
    media_type = ['top_media', 'recent_media']
    base_url = params['endpoint_url_base']
    ig_hashtag = models.IgHashtag.objects.filter(hashtag_word=keyword)
    if ig_hashtag.exists():
        hashtag_id = ig_hashtag[0].hashtag_id
    else:
        ig_hashtag_id_param = ( 
            f"v12.0/ig_hashtag_search?user_id={params['instagram_account_id']}"
            f"&q={keyword}&access_token={params['access_token']}"
        )
        ig_hashtag_id_url = base_url + ig_hashtag_id_param
        response = requests.get(ig_hashtag_id_url, timeout=5.0)
        content = json.loads(response.content)
        data = content['data']
        if not data:
            return []
        hashtag_id = data[0]['id']
        ig_hashtag.create(hashtag_id=hashtag_id, hashtag_word=keyword)

    fields = 'id,media_type,comments_count,like_count,media_url,permalink,children{media_type,media_url}'
    ig_hashtag_param = ( 
        f"v12.0/{hashtag_id}/{media_type[0]}?user_id={params['instagram_account_id']}"
        f"&fields={fields}&access_token={params['access_token']}"
    )
    ig_hashtag_url = base_url + ig_hashtag_param
    response = requests.get(ig_hashtag_url, timeout=5.0)
    contents = json.loads(response.content)
    
    posts_parameters_list = []
    for content in contents['data']:
        post_parameters_dict = {}
        if content['media_type'] == 'CAROUSEL_ALBUM':
            for child_content in content['children']['data']:
                if child_content['media_type'] == 'IMAGE':
                    media_url = child_content.get('media_url')
                    post_parameters_dict['media_url'] = media_url
                    post_parameters_dict['permalink'] = content['permalink']
                    post_parameters_dict['like_count'] = content.get('like_count')
                    post_parameters_dict['comments_count'] = content.get('comments_count')

                    break
                else:
                    continue
        elif content['media_type'] == 'IMAGE':
            post_parameters_dict['media_url'] = content.get('media_url')
            post_parameters_dict['permalink'] = content['permalink']
            post_parameters_dict['like_count'] = content.get('like_count')
            post_parameters_dict['comments_count'] = content.get('comments_count')
        else:
            continue
        
        if post_parameters_dict['media_url'] is not None:
            posts_parameters_list.append(post_parameters_dict)
    return posts_parameters_list
