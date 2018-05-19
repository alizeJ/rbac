def login_msg(request, user):
    permission_info = user.roles.all().values('permissions__title',
                                              'permissions__url',
                                              'permissions__pg__id',
                                              'permissions__code').distinct()

    temp = {}
    for i in permission_info:
        if i['permissions__pg__id'] not in temp:
            temp[i['permissions__pg__id']] = {'urls': [i['permissions__url']],
                                              'codes': [i['permissions__code']]}
        else:
            temp[i['permissions__pg__id']]['urls'].append(i['permissions__url'])
            temp[i['permissions__pg__id']]['codes'].append(i['permissions__code'])
    request.session['permissions_dict'] = temp
    print(temp)
