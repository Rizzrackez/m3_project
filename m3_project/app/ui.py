from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from django.contrib.auth.models import ContentType


class UserAddAndEditWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddAndEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'Username пользователя',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'Email',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__firstname = ext.ExtStringField(
            label=u'Имя пользователя',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label=u'Фамилия пользователя',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        # self.field__last_login = ext.ExtDateField(
        #     label=u'last login',
        #     name='last_login',
        #     anchor='100%',
        #     format='Y-m-d')
        #
        # self.field__date_joined = ext.ExtDateField(
        #     label=u'date joined',
        #     name='date_joined',
        #     anchor='100%',
        #     format='Y-m-d')

        self.field__is_active = ext.ExtCheckBox(
            label=u'Active',
            name='is_active',
            allow_blank=False,
            anchor='100%'
        )

        self.field__is_staff = ext.ExtCheckBox(
            label=u'is_staff',
            name='is_staff',
            allow_blank=False,
            anchor='100%'
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'is_superuser',
            name='is_superuser',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        super(UserAddAndEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__email,
            self.field__firstname,
            self.field__lastname,
            self.field__password,
            self.field__is_active,
            self.field__is_staff,
            self.field__is_superuser,
            # self.field__last_login,
            # self.field__date_joined,
        ))

    def set_params(self, params):
        super(UserAddAndEditWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddAndEditWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddAndEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        ct = list(ContentType.objects.all())
        ct_dict = tuple(zip(list(range(len(ct))), map(str, ct)))
        ((ct.id, ct.title) for ct in ContentType.objects.all()))
        

        self.field__content_type = make_combo_box(
            label=u'content type',
            name='content_type',
            allow_blank=False,
            anchor='100%',
            data=ct_dict)

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionAddAndEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionAddAndEditWindow, self).set_params(params)
        self.height = 'auto'
