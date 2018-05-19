from rbac.models import *


def initial_session(request, user):
    ################################## 用于判断左侧菜单是否闭合在自定义标签中使用 ###################################
    permission_info = user.roles.all().values('permissions__id',
                                              'permissions__title',
                                              'permissions__code',
                                              'permissions__url',
                                              'permissions__parent_id',
                                              'permissions__permission_group__menu__caption',
                                              'permissions__permission_group__menu__id',
                                              "permissions__permission_group__caption").distinct()
    # print(permission_info)
    permission_list = []
    for item in permission_info:
        temp = {
            'id': item['permissions__id'],
            'url': item['permissions__url'],
            'pid': item['permissions__parent_id'],
            'title': item['permissions__title'],
            'menu_id': item['permissions__permission_group__menu__id'],
            'menu': item['permissions__permission_group__menu__caption'],
        }
        permission_list.append(temp)
    print(permission_list)
    request.session['permission_list'] = permission_list


    # permissions_dict = {
    #     '2': {
    #         "urls": ["/orders/", ],
    #         "codes": ["list", 'delete', 'add']
    #     },
    # }

    ############################ 登录后用于内容的显示即有无---编辑，删除，增加按钮---下一次在中间件中判断 ###############
    temp = {}
    for i in permission_info:
        if i['permissions__permission_group__caption'] not in temp:
            temp[i['permissions__permission_group__caption']] = {'urls': [i['permissions__url']],
                                                                 'codes': [i["permissions__code"]]}
        else:
            temp[i['permissions__permission_group__caption']]['urls'].append(i['permissions__url'])
            temp[i['permissions__permission_group__caption']]['codes'].append(i["permissions__code"])

    # print(temp)
    request.session["permissions_dict"] = temp


