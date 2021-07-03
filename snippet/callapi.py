import requests
import json

from requests.api import get

print(requests.__version__)

# path = [{
#     'address':
#     '725 Hẻm số 7 Thành Thái, Phường 14, Quận 10, Hồ Chí Minh, Việt Nam'
# }, {
#     'address':
#     'Miss Ao Dai Building, 21 Nguyễn Trung Ngạn, Bến Nghé, Quận 1, Hồ Chí Minh, Vietnam'
# }]

# payload = {
#     'scopes': 'PublicApi.Access',
#     'grant_type': 'client_credentials',
#     'client_id': 'e6f2be5a-1bd3-462f-8e09-2d9476b9d5e8',
#     'client_secret': 'A3A594783D4E5166465493FA3DA0B768731A8183'
# }

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# r = requests.post('https://id.kiotviet.vn/connect/token',
#                   headers=headers,
#                   data=payload)

# print(r.url)
# print(r.text)

# r = requests.post('https://apistg.ahamove.com/v1/order/create',
#                   params=payload,
#                   headers=headers)

# print(r.url)

ENDURL = "https://public.kiotapi.com/"


def _do_request(uri,
                headers=None,
                params=None,
                json=None,
                data=None,
                type='POST',
                is_authen=True,
                token='',
                retailer=''):
    if params is None:
        params = {}
    if json is None:
        json = {}
    if data is None:
        data = {}
    if headers is None:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    if is_authen:
        headers['Authorization'] = 'Bearer ' + token
        headers['Retailer'] = retailer
    if type.upper() in 'GET':
        res = requests.get(ENDURL + uri,
                           params=params,
                           headers=headers,
                           data=data)
    elif type.upper() in 'POST':
        res = requests.post(ENDURL + uri,
                            params=params,
                            headers=headers,
                            data=data)
    else:
        res = None
    return res


def get_product_category(token, retailer):
    return _do_request(uri='categories',
                       type='GET',
                       token=token,
                       retailer=retailer)


def get_product_list(token, retailer):
    return _do_request(uri='products',
                       type='GET',
                       token=token,
                       retailer=retailer)


def get_product_attribute(token, retailer):
    return _do_request(uri='attributes/allwithdistinctvalue',
                       type='GET',
                       token=token,
                       retailer=retailer)


token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2MjE0MjYxODcsImV4cCI6MTYyMTUxMjU4NywiaXNzIjoiaHR0cDovL2lkLmtpb3R2aWV0LnZuIiwiYXVkIjpbImh0dHA6Ly9pZC5raW90dmlldC52bi9yZXNvdXJjZXMiLCJLaW90VmlldC5BcGkuUHVibGljIl0sImNsaWVudF9pZCI6ImU2ZjJiZTVhLTFiZDMtNDYyZi04ZTA5LTJkOTQ3NmI5ZDVlOCIsImNsaWVudF9SZXRhaWxlckNvZGUiOiJib29iaWVzIiwiY2xpZW50X1JldGFpbGVySWQiOiI5MzgxMDciLCJjbGllbnRfVXNlcklkIjoiMzE0MjciLCJjbGllbnRfU2Vuc2l0aXZlQXBpIjoiVHJ1ZSIsInNjb3BlIjpbIlB1YmxpY0FwaS5BY2Nlc3MiXX0.kL2lgm2LMNt9VkRv2MgsnEPT-RGE_VtFo89xcBenFswJIk47BrNYjxpaE_Ccy5JuDhlWgAD3fwAs1MrDtKrjCXJfWhu3bLSzGo4h_jIwNXuYrPAFNG41g3K73wUCNaFDqWlgCvi1pitJLmZyIGmkMj8caMfttzoBHo8LzsjKA_Lx6taRrZO8ba_z7soHOAF4yh0-nXPWcBtbir5CQKmnvysBzEwy1-tZCYvV8ZZc6stkjT2Ru53s3kzH1A7EPaekU7mx5j50xwk5IuzHnp1aKAq3AnAlTt6bwgtN1YZGQR4A3W4f0hJ5yNdygYOL09YfV0l2cq1IlHaNzBKjw2050g'

retailer = 'boobies'

r = get_product_category(token, retailer)
print(r.text)
print(r.url)
