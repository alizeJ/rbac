from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class M1(MiddlewareMixin):

    def process_request(self, request):
        path = request.path_info
        white_list = ['/login/$', '/admin/.*', '/$']
        import re
        for i in white_list:
            ret = re.match(i, path)
            if ret:
                return None
        """
        permission_dict = {
            2: {
                urls: ['/users/', ]
                codes: ['list', ]
            }
        }
        """

        permissions_dict = request.session.get('permissions_dict')
        if not permissions_dict:
            return redirect('/login/')

        for item in permissions_dict.values():
            urls = item['urls']
            codes = item['codes']
            for url in urls:
                url = '^%s$' % url
                ret = re.match(url, path)
                if ret:
                    request.permission_codes = codes
                    return None
        return HttpResponse('没有权限')
