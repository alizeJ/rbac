from django.template import Library
register = Library()


@register.inclusion_tag('left_menu.html')
def get_left_menu(request):
    permission_list = request.session.get('permission_list')

    # 生成一个temp= [{'1':{...}}...]
    temp_dict = {}
    for item in permission_list:
        if item['pid'] is None:
            item['active'] = False
            temp_dict[item['id']] = item

    import re
    current_path = request.path_info
    print(current_path)
    for item in permission_list:
        url = '^%s$' % item['url']
        ret = re.match(url, current_path)
        if ret:
            if item['pid']:
                temp_dict[item['id']]['active'] = True
            else:
                item['active'] = True
            break

    menu_dict = {}
    for i in temp_dict.values():
        if i['menu_id'] in menu_dict:
            if i['active']:
                menu_dict[i['menu_id']]['active'] = True
            temp = {'title': i['title'], 'url': i['url'], 'active': i['active']}
            menu_dict[i['menu_id']]['children'].append(temp)
        else:
            menu_dict[i['menu_id']] = {
                'title': i['menu'],
                'active': i['active'],
                'children': [{'title': i['title'], 'url': i['url'], 'active': i['active']}]
            }
    return {'menu_dict': menu_dict}



from wsgiref import simple_server,headers
from io import StringIO
