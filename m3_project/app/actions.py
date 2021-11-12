import objectpack
from django.contrib.auth.models import User, ContentType, Group, Permission
from m3 import ApplicationLogicException
from objectpack.actions import ObjectPack
from app import ui
from app.app_services import check_valid_email_address


class UserPack(ObjectPack):

    model = User

    columns = [
        {
            'data_index': 'username',
            'header': u'Username пользователя',
        },
        {
            'data_index': 'email',
            'header': u'Email',
        },
        {
            'data_index': 'first_name',
            'header': u'Имя пользователя',
        },
        {
            'data_index': 'last_name',
            'header': u'Фамилия пользователя',
        },
        {
            'data_index': 'is_active',
            'header': u'active',
        },
        {
            'data_index': 'is_staff',
            'header': u'is stuff',
        },
        {
            'data_index': 'is_superuser',
            'header': u'is superuser',
        },
        {
            'data_index': 'date_joined',
            'header': u'date joined',
        },

    ]

    add_to_menu = True
    add_window = edit_window = ui.UserAddAndEditWindow

    def save_row(self, obj, create_new, request, context):

        if not check_valid_email_address(obj.email):
            raise ApplicationLogicException(
                u'Неправильно введен Email адрес!')

        users = User.objects.all()
        usernames = [user.username for user in users]
        obj_username = obj.username

        try:
            super(UserPack, self).save_row(obj, create_new, request, context)
            obj.set_password(obj.password)
            obj.save()
        except:
            if obj_username in usernames:
                raise ApplicationLogicException(
                    u'Пользователь с таким именем уже существует!')


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)
    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = Permission
    add_window = edit_window = ui.PermissionAddAndEditWindow
    add_to_menu = True

    def save_row(self, obj, create_new, request, context):
        obj.content_type = ContentType.objects.all()[int(context.content_type)]
        super(PermissionPack, self).save_row(obj, create_new, request, context)


