from django.urls import path
from users import api, views

urlpatterns = [
    path('send_code/', api.SendCode.as_view()),
    path('resend_code/', api.SendCode.as_view()),
    path('verify_code/', api.VerifyCode.as_view()),
    path('register/', api.RegisterAPIView.as_view()),
    # path('login', api.LoginAPIView.as_view()),
    # path('user', api.UserAPIView.as_view()),
    # path('refresh', api.RefreshAPIView.as_view()),
    # path('logout', api.LogoutAPIView.as_view())

    path('users/', views.UserList.as_view()),
    # path('users/<pk>/', views.UserDetails.as_view()),
    # path('groups/', views.GroupList.as_view())
]