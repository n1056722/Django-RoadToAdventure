"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views as views_users
from personalJourneys import views as views_personalJourney
#from personalJourneys import views as views_pj
urlpatterns = [
    url(r'^$', views_users.index, name='index'),
    url(r'^User/hello', views_users.hello, name='users_hello'),
    url(r'^User/ya', views_users.ya, name='users_ya'),
    url(r'^User/signIn', views_users.signIn, name='users_signIn'),
    url(r'^User/signUp', views_users.signUp, name='users_signUp'),
    url(r'^User/updatePassword', views_users.updatePassword, name='users_updatePassword'),
    #url(r'^User/updatePicture', views_users.updatePicture, name='users_updatePicture'),
    #url(r'^Picture/create', views_users.create, name='users_create'),
    url(r'^Friend/create', views_users.createFriend, name='users_createFriend'),
    url(r'^Friend/delete', views_users.deleteFriend, name='users_deleteFriend'),
    url(r'^Friend/getStrangerList', views_users.getStrangerList, name='users_getStrangerList'),
    url(r'^Friend/getFriendList', views_users.getFriendList, name='users_getFriendList'),
    url(r'^FriendChat/createFriendChat', views_users.createFriendChat, name='users_createFriendChat'),
    url(r'^FriendChat/getChatList', views_users.getChatList, name='users_getChatList'),
    url(r'^PersonalJourney/Create', views_personalJourney.Create, name='personalJourneys_Create'),
    #url(r'^PersonalJourney/Update', views_personalJourneys.Update, name='personalJourneys_Update'),
    #url(r'^PersonalJourney/getList', views_personalJourneys.getList, name='personalJourneys_getList'),
    url(r'^admin/', admin.site.urls),
]
