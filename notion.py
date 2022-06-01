# 删除页面：delete_page(page_id)
import requests

# notion基本参数
token = 'secret_XgyUrFiMmBtXhOYYWqz7Df6pBOZFbFeo4Q0Z8YtNbs7'
headers = {
    'Notion-Version': '2021-05-13',
    'Authorization': 'Bearer '+token,
}


def delete_page(page_id):
    body = {
        'archived': True
    }

    url = 'https://api.notion.com/v1/pages/'+page_id
    notion = requests.patch(url, headers=headers, json=body)

    return 0

 # 更新页面属性：updata_page_properties(page_id,body,station)
# 其中的station用来说明你处理对象是否成功更新了属性
def updata_page_properties(page_id,body,station):
    url = 'https://api.notion.com/v1/pages/'+page_id
    notion = requests.patch(url,headers=headers,json=body)

    if notion.status_code == 200:
        print(station+'·更新成功')
    else:
        print(station+'·更新失败')

    return 0

# 获取页面属性：get_page_information(page_id)
# 返回的是字典型数据，数据结构同上面的body结构相似，而内容是对应页面属性值。
def get_page_information(page_id):
    url = 'https://api.notion.com/v1/pages/'+page_id
    notion_page = requests.get(url,headers=headers)
    result = notion_page.json()
    if notion_page.status_code == 200:
        print('页面属性获取成功')
    else:
        print('页面属性获取失败')

    return result

# 4. 获取数据库中的每条数据：DataBase_item_query(query_database_id)

def DataBase_item_query(query_database_id):
    url_notion_block = 'https://api.notion.com/v1/databases/'+query_database_id+'/query'
    res_notion = requests.post(url_notion_block,headers=headers)
    S_0 = res_notion.json()
    res_travel = S_0['results']
    if_continue = len(res_travel)
    if if_continue>0:
        while if_continue%100 == 0:
            body = {
                'start_cursor' : res_travel[-1]['id']
            }
            res_notion_plus = requests.post(url_notion_block,headers=headers,json = body)
            S_0plus = res_notion_plus.json()
            res_travel_plus = S_0plus['results']
            for i in res_travel_plus:
                if i['id'] == res_travel[-1]['id']:
                    continue
                res_travel.append(i)
            if_continue = len(res_travel_plus)
    return res_travel

# 5. 向database数据库增加数据条目：DataBase_additem(database_id,body_properties,station)

def DataBase_additem(database_id,body_properties,station):

    body = {
        'properties': {},
        'parent': {'type': 'database_id', 'database_id': database_id},
    }
    body.update(body_properties)

    url_notion_additem = 'https://api.notion.com/v1/pages'
    notion_additem = requests.post(url_notion_additem,headers=headers,json=body)

    print(notion_additem.text)

    if notion_additem.status_code == 200:
        print(station+'·更新成功')
    else:
        print(station+'·更新失败')


def DataBase_additem111(database_id,time,content,num):
    body = {
    "parent": {"type": "database_id", "database_id": database_id},
    "properties": {},
    }

    # body111 = body_properties_input(body,'时间','rich_text',time)
    body111 = body_properties_input(body,'价格','rich_text',num)
    body111 = body_properties_input(body,'内容','rich_text',content)
    body.update(body111)

    url_notion_additem = 'https://api.notion.com/v1/pages'
    notion_additem = requests.post(url_notion_additem,  headers={"Authorization": "Bearer " + "secret_39U6k89PZo9SD8qOCjHLa3HIdrLtQH85kbP3Ut6mVN3", "Notion-Version": "2021-05-13"}, json=body)

    print(notion_additem.text)

    if notion_additem.status_code == 200:
        print('·更新成功')
    else:
        print('·更新失败')

# 6.1 获取指定页面属性的指定属性值：pageid_information_pick(page_id,label)

def pageid_information_pick(page_id,label):
    x = get_page_information(page_id)

    if label == 'id':
        output=x['id']
    else:
        type_x = x['properties'][label]['type']

        if type_x == 'checkbox':
            output = x['properties'][label]['checkbox']

        if type_x == 'date':
            output = x['properties'][label]['date']['start']

        if type_x == 'select':
            output = x['properties'][label]['select']['name']

        if type_x == 'rich_text':
            output = x['properties'][label]['rich_text'][0]['plain_text']

        if type_x == 'title':
            output = x['properties'][label]['title'][0]['plain_text']

        if type_x == 'number':
            output = x['properties'][label]['number']

    return output


# 6.2 获取body结构中的指定属性值：item_information_pick(item,label)

def item_information_pick(item,label):
    x = item

    if label == 'id':
        output=x['id']
    else:
        type_x = x['properties'][label]['type']

        if type_x == 'checkbox':
            output = x['properties'][label]['checkbox']

        if type_x == 'date':
            output = x['properties'][label]['date']['start']

        if type_x == 'select':
            output = x['properties'][label]['select']['name']

        if type_x == 'rich_text':
            output = x['properties'][label]['rich_text'][0]['plain_text']

        if type_x == 'title':
            output = x['properties'][label]['title'][0]['plain_text']

        if type_x == 'number':
            output = x['properties'][label]['number']

    return output

# 7.1 body属性值字典数据的建立（多参数）：body_properties_input(body,label,type_x,data)

def body_properties_input(body,label,type_x,data):

    if type_x == 'checkbox':
        body['properties'].update({label:{'type': 'checkbox', 'checkbox': data}})

    if type_x == 'date':
        body['properties'].update({label:{'type': 'date', 'date': {'start': data, 'end': None}}})

    if type_x == 'select':
        body['properties'].update({label:{'type': 'select', 'select': {'name': data}}})
# body,'时间','rich_text',time
    if type_x == 'rich_text':
        body['properties'].update({label:{'type': 'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': data},  'plain_text': data}]}})

    if type_x == 'title':
        body['properties'].update({label:{'id': 'title', 'type': 'title', 'title': [{'type': 'text', 'text': {'content': data}, 'plain_text': data}]}})

    if type_x == 'number':
        body['properties'].update({label:{'type': 'number', 'number': data}})

    return body


# 7.2 body属性值字典数据的建立（单参数）：body_propertie_input(label,type_x,data)

def body_propertie_input(label,type_x,data):

    body={
    'properties':{}
    }

    if type_x == 'checkbox':
        body['properties'].update({label:{'type': 'checkbox', 'checkbox': data}})

    if type_x == 'date':
        body['properties'].update({label:{'type': 'date', 'date': {'start': data, 'end': None}}})

    if type_x == 'select':
        body['properties'].update({label:{'type': 'select', 'select': {'name': data}}})

    if type_x == 'rich_text':
        body['properties'].update({label:{'type': 'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': data},  'plain_text': data}]}})

    if type_x == 'title':
        body['properties'].update({label:{'id': 'title', 'type': 'title', 'title': [{'type': 'text', 'text': {'content': data}, 'plain_text': data}]}})

    if type_x == 'number':
        body['properties'].update({label:{'type': 'number', 'number': data}})

    return body

# 8.1 从database数据库中筛选出符合条件的条目：select_items_form_Databaseid(Database_id,label,value)
# 返回值为列表型数据，该数据符合你的筛选条件的

def select_items_form_Databaseid(Database_id,label,value):
    items = DataBase_item_query(Database_id)
    items_pick = []

    for item in items:
        if item_information_pick(item,label) == value:
            items_pick.append(item)

    return items_pick


# 8.2 从database数据库的条目中筛选出符合条件的条目：select_items_form_Databaseitems(items,label,value)
# 返回值为列表型数据，该数据符合你的筛选条件的

def select_items_form_Databaseitems(items,label,value):
    items_pick = []

    for item in items:
        if item_information_pick(item,label) == value:
            items_pick.append(item)

    return items_pick

