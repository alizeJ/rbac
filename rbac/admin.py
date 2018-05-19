from django.contrib import admin
# from .models import *
# # Register your models here.
# admin.site.register(UserInfo)
# admin.site.register(Role)
# admin.site.register(Menu)
#
#
# # class PermissionConfig(admin.ModelAdmin):
# #     list_display = ["id", "title", "url"]
# #     ordering = ["id"]
# #
# #
# # admin.site.register(Permission, PermissionConfig)
# class PermissionConfig(admin.ModelAdmin):
#     # ordering = ['id']
#     list_display = ['id', 'title', 'url', 'code', 'permission_group', 'parent']
#     # list_display_links = ['title']
#     # list_filter = ['permission_group']
#     # raw_id_fields = ('permission_group', )
#     # list_editable = ['permission_group']
#     # fields = ['permission_group']
#     # readonly_fields = ['parent']
#
#     def foo(self, request, queryset):
#         queryset.delete()
#
#     foo.short_description = '删除'
#     actions = [foo, ]
#
#
# admin.site.register(Permission, PermissionConfig)
#
#
# class PermissionGroupConfig(admin.ModelAdmin):
#     list_display = ['caption', 'menu']
#
#
# admin.site.register(PermissionGroup, PermissionGroupConfig)
from .models import *
admin.site.register(UserInfo)
admin.site.register(Role)


class PermissionConfig(admin.ModelAdmin):
    list_display = ['id', 'title', 'code', 'pg']
    ordering = ['id']


admin.site.register(Permission, PermissionConfig)
admin.site.register(PermissionGroup)
