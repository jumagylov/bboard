from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.apps import AppConfig
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .models import AdvUser
#from .forms import ChangeUserInfoForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView



def index(request):
    return render(request, 'main/index.html')

class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Доска объявлений'

def outher_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
    template_name = 'main/Login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')

class BBLogoutView(LoginRequiredMixin):
    template_name = 'main/logout.html'

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес элоктроной почты')
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Личные данные пользователя изменены'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Личные данные пользователя изменены'




