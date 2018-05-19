from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class M2(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path_info
        print(current_path)
        white_list = ['/login/$', '/$', '/admin/.*']
        import re
        for val in white_list:
            ret = re.match(val, current_path)
            if ret:
                return None
        # 未登陆
        permissions_dict = request.session.get('permissions_dict')
        if not permissions_dict:
            return redirect('/login/')

        current_path = request.path_info
        for item in permissions_dict.values():
            for url in item['urls']:
                url = '^%s$' % url
                ret = re.match(url, current_path)
                if ret:
                    request.permission_codes = item['codes']
                    return None
        return HttpResponse('没有权限')