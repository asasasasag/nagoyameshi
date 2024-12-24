from django.urls import path

from . import views

urlpatterns = [
    path("user-detail/<int:pk>/", views.UserDetailView.as_view(),name="user_detail"),
    path("user-update/<int:pk>/", views.UserUpdateView.as_view(),name="user_update"),
    path("subscribe-register/", views.SubscribeRegisterView.as_view(),name="subscribe_register"),
    path("subscribe-cancel/", views.SubscribeCancelView.as_view(),name="subscribe_cancel"),
    
    path("management/user-list",views.ManagementUserListView.as_view(), name="user_list"),
    path("management/restaurant-manage-list",views.ManagementRestaurantListView.as_view(), name="restaurant_manage_list"),
    path("management/restaurant-update/<int:pk>/",views.ManagementRestaurantUpdateView.as_view(), name="restaurant_update"),

    path("management/category-list",views.ManagementCategoryListView.as_view(), name="category_list"),
    path("management/sales/",views.ManagementSalesListView.as_view(), name="sales")

]
