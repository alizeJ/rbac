from django.db import models

# Create your models here.


# class UserInfo(models.Model):
#     name = models.CharField(max_length=32)
#     pwd = models.CharField(max_length=16, default='1234')
#     email = models.EmailField()
#     roles = models.ManyToManyField(to='Role')
#
#     def __str__(self):
#         return self.name
#
#
# class Role(models.Model):
#     title = models.CharField(max_length=32)
#     permissions = models.ManyToManyField(to='Permission')
#
#     def __str__(self):
#         return self.title
#
#
# class Permission(models.Model):
#     title = models.CharField(max_length=32)
#     url = models.CharField(max_length=32)
#     permission_group = models.ForeignKey(to='PermissionGroup')
#     code = models.CharField(max_length=32, default='')
#     parent = models.ForeignKey(to='self', default=1, null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
#
# class PermissionGroup(models.Model):
#     caption = models.CharField(max_length=32)
#     menu = models.ForeignKey(to='Menu', default=1)
#
#     def __str__(self):
#         return self.caption
#
#
# class Menu(models.Model):
#     caption = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.caption


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField()
    roles = models.ManyToManyField(to='Role')

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(to='Permission')

    def __str__(self):
        return self.title


class Permission(models.Model):
    title = models.CharField(max_length=32)
    # 用户的权限就是一个个的url
    url = models.CharField(max_length=32)
    # menu = models.ForeignKey(to='Menu')
    code = models.CharField(max_length=32, default='')
    pg = models.ForeignKey(to='PermissionGroup')

    def __str__(self):
        return self.title


class PermissionGroup(models.Model):
    group = models.CharField(max_length=32)
    menu = models.ForeignKey(to='Menu')

    def __str__(self):
        return self.group


class Menu(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return self.caption
