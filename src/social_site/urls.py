from django.conf.urls import url
from . import views
app_name='social_site'
urlpatterns = [
    url(r'^$', views.Homeview, name='home'),
    #url(r'^login/$',views.LoginFormView.as_view(),name='login'),
    url(r'^login_check/$',views.LoginCheckFormView.as_view(),name='login_check'),

    url(r'^logout/$',views.logout_view,name='logout_view'),

    url(r'register/$',views.Sign_Up.as_view(),name='register'),
    url(r'^user_check/$',views.check, name='check'),
]