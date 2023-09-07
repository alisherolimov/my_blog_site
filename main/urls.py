from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('courses/', course_view, name='course_url'),
    path('elements/', elements_view, name='elements_url'),
    path('news/', news_view, name='news_url'),
    path('contact/', contact_view, name='contact_url'),
    path('new-detail/<int:pk>/', new_post_view, name='new_post_url'),
    path('', login_view, name="login_url"),
    path('log-up/', signup_view, name="signup_url"),
    path('profile/', profile_view, name="profile_url"),
    path('logout/', logout_view, name="logout_url"),
    path('delete_user/<int:pk>/', delete_user_view, name="delete_user_url"),
    path('create_comment/<int:pk>/ ', create_comment_view, name="create_comment_url"),
]