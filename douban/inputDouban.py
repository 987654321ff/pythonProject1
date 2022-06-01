import douban
import notion

database_id='d718b667-c4b7-415f-9d43-40b68d571a4b'

panduan = 1
while (panduan):
    print('-----------------------------')
    Movie_id = input('请输入输入电影代码：\n')
    search_result = douban.douban_Movie_Notion(Movie_id)

    body = {
        'properties': {}
    }
# 35008440
    body = notion.body_properties_input(body,'电影名称与年份','rich_text',search_result['电影名称与年份'])
    body = notion.body_properties_input(body,'导演','rich_text',search_result['基本信息']['导演'])
    body = notion.body_properties_input(body,'编剧','rich_text',search_result['基本信息']['编剧'])
    body = notion.body_properties_input(body,'主演','rich_text',search_result['基本信息']['主演'])
    body = notion.body_properties_input(body,'上映日期','rich_text',search_result['基本信息']['上映日期'])
    body = notion.body_properties_input(body,'片长','rich_text',search_result['基本信息']['片长'])
    body = notion.body_properties_input(body,'又名','rich_text',search_result['基本信息']['又名'])
    body = notion.body_properties_input(body,'简介','rich_text',search_result['简介'])
    body = notion.body_properties_input(body,'评分','rich_text',search_result['评分分数']+'('+search_result['评分人数']+')')
    body = notion.body_properties_input(body,'评分好于','rich_text',search_result['评分好于'])
    body = notion.body_properties_input(body,'图片连接','files',search_result['图片连接'])
    body = notion.body_properties_input(body,'类型','multi_select',search_result['基本信息']['类型'].replace(" ", "").split('/'))
    body = notion.body_properties_input(body,'制片国家/地区','multi_select',search_result['基本信息']['制片国家/地区'].replace(" ", "").split('/'))
    body = notion.body_properties_input(body,'语言','multi_select',search_result['基本信息']['语言'].replace(" ", "").split('/'))
    notion.DataBase_additem(database_id,body,search_result['电影名称与年份'])
    panduan = int(input('是否继续添加：1：继续添加，0：退出\n'))
