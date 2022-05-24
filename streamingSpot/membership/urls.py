from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipView.as_view(), name='select'),
    path('/memberships/', views.MembershipsView.as_view(), name='memberships'),
    path('/usermemberships/', views.UserMembershipsView.as_view(),
         name='usermemberships'),
    path('/subscriptions/', views.SubscriptionsView.as_view(), name='subscriptions'),

]
