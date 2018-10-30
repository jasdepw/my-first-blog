from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#name='post_list'는 URL에 이름을 붙인 것으로 뷰를 식별