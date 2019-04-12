import io

from django import forms
from django.forms import ModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import ListView
from openpyxl import Workbook

from app.models import User
from app.templatetags.bizz import calc_bizz
from app.templatetags.perms import check_perms


def download_list(request):
    users = User.objects.all()

    wb = Workbook()
    ws = wb.active
    ws.title = "Users"

    ws.append(["Username", "Date of birth", "Number", "Eligible", "Bizz"])

    for user in users:
        ws.append([
            user.username,
            user.date_of_birth,
            user.random_num,
            check_perms(user),
            calc_bizz(user.random_num),
        ])

    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 10

    f = io.BytesIO()
    wb.save(f)

    response = HttpResponse(bytes(f.getbuffer()), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="users.xlsx"'
    return response


class UserList(ListView):
    queryset = User.objects.order_by('id')
    template_name = "user_list.html"
    context_object_name = 'user_list'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'date_of_birth', 'random_num']

    field_order = ['username', 'password', 'date_of_birth', 'random_num']

    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].required = False
        self.fields['random_num'].required = False

    def save(self, commit=True):
        passwd = self.cleaned_data['password']
        if len(passwd) > 0:
            self.instance.set_password(passwd)
        return super().save(commit=commit)


class UserCreateView(CreateView):
    form_class = UserForm
    model = User
    template_name = "user_edit.html"
    success_url = "/list"


class UserUpdateView(UpdateView):
    form_class = UserForm
    model = User
    template_name = "user_edit.html"
    success_url = "/list"


class UserDeleteView(DeleteView):
    form_class = UserForm
    model = User
    template_name = "user_delete.html"
    success_url = "/list"


class UserDetailView(DetailView):
    form_class = UserForm
    model = User
    template_name = "user_view.html"
