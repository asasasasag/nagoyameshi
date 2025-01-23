from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from . import passwords_reset

urlpatterns = [
    path("user-detail/<int:pk>/", views.UserDetailView.as_view(),name="user_detail"),
    path("user-update/<int:pk>/", views.UserUpdateView.as_view(),name="user_update"),
    path("subscribe-register/", views.SubscribeRegisterView.as_view(),name="subscribe_register"),
    path("subscribe-cancel/", views.SubscribeCancelView.as_view(),name="subscribe_cancel"),
    path("subscribe-payment/", views.SubscribePaymentView.as_view(),name="subscribe_payment"),
    
    path("management/user-list",views.ManagementUserListView.as_view(), name="user_list"),
    path("management/user-list-update/<int:pk>/", views.ManagementUserListUpdateView.as_view(), name="user_list_update"),
    path("management/user-delete/<int:pk>/", views.ManagementUserDeleteView.as_view(), name='user_delete'),

    path("management/restaurant-manage-list",views.ManagementRestaurantListView.as_view(), name="restaurant_manage_list"),
    path("management/restaurant-create/",views.ManagementRestaurantCreateView.as_view(), name="restaurant_create"),
    path("management/restaurant-update/<int:pk>/",views.ManagementRestaurantUpdateView.as_view(), name="restaurant_update"),
    path("management/restaurant-delete/<int:pk>/",views.ManagementRestaurantDeleteView.as_view(), name="restaurant_delete"),

    path("user/password_change_form/", auth_views.PasswordChangeView.as_view(template_name='user/password_change.html'), name='password_change_form'),   # 追加
    path("user/password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_finish.html'), name='password_change_done'), # 追加

    path("user/password_reset/", passwords_reset.PasswordReset.as_view(), name='password_reset'), #追加
    path("user/password_reset_done/", passwords_reset.PasswordResetDone.as_view(), name='password_reset_done'), #追加
    path("user/password_reset_confirm/<uidb64>/<token>/", passwords_reset.PasswordResetConfirm.as_view(), name='password_reset_confirm'), #追加
    path("user/password_reset_complete/", passwords_reset.PasswordResetComplete.as_view(), name='password_reset_complete'), #追加

    path("management/category-list",views.ManagementCategoryListView.as_view(), name="category_list"),
    path("management/category-create/",views.ManagementCategoryCreateView.as_view(), name="category_create"),
    path("management/category-update/<int:pk>/",views.ManagementCategoryUpdateView.as_view(), name="category_update"),
    path("management/category-delete/<int:pk>/",views.ManagementCategoryDeleteView.as_view(), name="category_delete"),

    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),

    path("management/sales/",views.ManagementSalesListView.as_view(), name="sales")

]
