import requests
import openpyxl  # excel模块，属于第三方库可能需要下载该模块，我用过CSV模块但是中文编码有些问题所以没用了，改用该模块了

token = 'secret_RpQVQpPJatwExtsyoG6dryPAKmZ2c0Ediaauq8eNhrc'
headers = {
    'Notion-Version': '2021-05-13',  # 在新版中必须加入版本信息
    'Authorization': 'Bearer ' + token,  # 这一行也必须要有
}

database_id = '573dc1b5-d01c-4070-9a9c-c8aba0329877'
url_notion = 'https://api.notion.com/v1/databases/' + database_id + '/query'

res_notion = requests.post(url_notion, headers=headers)
S_0 = res_notion.json()
res_travel = S_0['results']
print(res_travel)

wb = openpyxl.Workbook()
sheet = wb.active
row = ['起点', '终点', '划分', '经纬度']
sheet.append(row)

for i in res_travel:
    item_object = i['object']
    item_id = i['id']
    item_type = i['parent']['type']
    item_database_id = i['parent']['database_id']
    item_properties = i['properties']

    place_start = item_properties['起点']['rich_text'][0]['text']['content']
    city_start = place_start.split('·')[0]
    address_start = place_start.split('·')[1]

    place_end = item_properties['终点']['rich_text'][0]['text']['content']
    city_end = place_end.split('·')[0]
    address_end = place_end.split('·')[1]

    key_gaode = 'c3f6d43681099e22d591c33dadc1ba05'
    url_gaode_1 = 'http://restapi.amap.com/v3/geocode/geo?key=' + key_gaode + '&address=' + address_start + '&city=' + city_start
    url_gaode_2 = 'http://restapi.amap.com/v3/geocode/geo?key=' + key_gaode + '&address=' + address_end + '&city=' + city_end

    S_1 = requests.get(url_gaode_1)
    S_2 = requests.get(url_gaode_2)
    bs_s1 = S_1.json()
    print(bs_s1)
    bs_s2 = S_2.json()
    position_start = bs_s1['geocodes'][0]['location']
    position_end = bs_s2['geocodes'][0]['location']
    style_output = '[' + position_start + '],' + '[' + position_end + ']'

    sheet.append([city_start, city_end, ' ', style_output])

    body = {
        "properties": {
            '坐标(起-终)': {
                'id': 'y[<<',
                'type': 'rich_text',
                'rich_text': [{
                    'type': 'text',
                    'text': {
                        'content': style_output,
                        'link': None
                    },
                    'annotations': {
                        'bold': False,
                        'italic': False,
                        'strikethrough': False,
                        'underline': False,
                        'code': False,
                        'color': 'default'
                    },
                    'plain_text': style_output,
                    'href': None
                }]
            },
        },
    }

    url_notion_page = 'https://api.notion.com/v1/pages/' + item_id
    ll = requests.patch(url_notion_page, headers=headers, json=body)
    if ll.status_code == 200:
        print('notion属性已更新成功')

wb.save('Travel_map.xlsx')
