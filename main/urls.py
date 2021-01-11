from django.urls import path
from .views import *

app_name = 'main'


class BBPasswordChangeView(object):
    pass


urlpatterns =[
    path('accounts/profile/change/', ChangeUserInfoView.as_view(),name='profile_change'),
    path('accounts/logout/', BBLoginView.as_view(), name='logout'),
    path('account/password/change/', BBPasswordChangeView.as_view(),
                                                name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', outher_page,name='other'),
    path('', index, name='index'),
]