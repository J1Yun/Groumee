"""calendarproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from groupmeet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grouplist/<str:id>',views.getuserGroupList,name="getuserGroupList"),
    path('group/<str:id>',views.groupCalendar_view,name="groupCalendar_view"),
    path('group/<str:id>/addschedule', views.createGroupSchedule, name="createGroupSchedule"),
    path('group/<str:id>/addcomment', views.addComment, name="addComment"),
    path('addschedule/<str:id>', views.allowRegister, name="allowRegister"),
    path('usercalendar/<str:user_id>/', views.userCalendar_view, name="userCalendar_view"),
    path('usercalendar/<str:user_id>/show', views.show_userschedule, name="show-userschedule"),
    path('usercalendar/delete', views.delete_userschedule, name="delete-userschedule"),
]