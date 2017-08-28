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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
# views
from users import views as views_users
from personalJourneys import views as views_personalJourney
from groups import views as views_groups
from groupJourneys import views as views_groupJourneys
urlpatterns = [
    url(r'^$', views_users.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^Picture/Create', views_users.createPicture, name='users_create'),

    url(r'^User/Login', views_users.login, name='users_login'),
    url(r'^User/SignUp', views_users.signUp, name='users_signUp'),
    url(r'^User/UpdatePassword', views_users.updatePassword, name='users_updatePassword'),
    url(r'^User/ForgetPassword', views_users.forgetPassword, name='users_forgetPassword'),
    url(r'^User/VerifyCode', views_users.verifyCode, name='users_verifyCode'),
    url(r'^User/ResetPassword', views_users.resetPassword, name='users_resetPassword'),

    url(r'^Friend/Create', views_users.createFriend, name='users_createFriend'),
    url(r'^Friend/Delete', views_users.deleteFriend, name='users_deleteFriend'),
    url(r'^Friend/GetStrangerList', views_users.getStrangerList, name='users_getStrangerList'),
    url(r'^Friend/GetFriendList', views_users.getFriendList, name='users_getFriendList'),

    url(r'^FriendChat/Create', views_users.createFriendChat, name='users_createFriendChat'),
    url(r'^FriendChat/GetList', views_users.getChatList, name='users_getChatList'),

    url(r'^PersonalJourney/Create', views_personalJourney.createPersonalJourney, name='personalJourneys_createPersonalJourney'),
    url(r'^PersonalJourney/Update', views_personalJourney.updatePersonalJourney, name='personalJourneys_updatePersonalJourney'),
    url(r'^PersonalJourney/GetList', views_personalJourney.getPersonalJourneyList, name='personalJourneys_getPersonalJourneyList'),
    url(r'^PersonalJourney/Get', views_personalJourney.getPersonalJourney, name='personalJourneys_getPersonalJourney'),
    url(r'^PersonalJourneyComment/Create', views_personalJourney.createPersonalJourneyComment, name='personalJourneys_createPersonalJourneyComment'),
    url(r'^PersonalJourneyDetail/Create', views_personalJourney.createPersonalJourneyDetail, name='personalJourneys_createPersonalJourneyDetail'),
    url(r'^PersonalJourneyDetail/GetAll', views_personalJourney.getAllPersonalJourneyDetail, name='personalJourneys_getPersonalJourneyDetailList'),

    url(r'^Group/Create', views_groups.createGroup, name='groups_createGroup'),
    url(r'^Group/Update', views_groups.updateGroup, name='groups_updateGroup'),
    url(r'^Group/GetList', views_groups.getGroupList, name='groups_getGroupList'),
    url(r'^Group/Get', views_groups.getGroup, name='groups_getGroup'),
    url(r'^GroupUser/Create', views_groups.createGroupUser, name='groups_createGroupUser'),
    url(r'^GroupUser/Update', views_groups.updateGroupUser, name='groups_updateGroupUser'),
    url(r'^GroupUser/Delete', views_groups.deleteGroupUser, name='groups_deleteGroupUser'),
    url(r'^GroupChat/Create', views_groups.createGroupChat, name='groups_createGroupChat'),
    url(r'^GroupChat/GetList', views_groups.getGroupChatList, name='groups_getGroupChatList'),

    url(r'^GroupJourney/Create', views_groupJourneys.createGroupJourney, name='groupJourneys_createGroupJourney'),
    url(r'^GroupJourney/Update', views_groupJourneys.updateGroupJourney, name='groupJourneys_updateGroupJourney'),
    url(r'^GroupJourney/GetList', views_groupJourneys.getGroupJourneyList, name='groupJourneys_getGroupJourneyList'),
    url(r'^GroupJourney/Get', views_groupJourneys.getGroupJourney, name='groupJourneys_getGroupJourney'),
    url(r'^GroupJourneyDetail/Create', views_groupJourneys.createGroupJourneyDetail, name='groupJourneys_createGroupJourneyDetail'),
    url(r'^GroupJourneyDetail/GetAll', views_groupJourneys.getGroupJourneyAll, name='groupJourneys_getGroupJourneyAll'),

] + static('/images/', document_root = settings.MEDIA_ROOT)
