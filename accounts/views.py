from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from . import forms
from . import models
from .mixins import onlyManagementUserMixin

from restaurant.models import Category
from restaurant.models import Restaurant
from restaurant.models import Sales



# 会員登録
class UserDetailView(generic.DetailView):
    model = models.CustomUser
    template_name = 'user/user_detail.html'
 
class UserUpdateView(generic.UpdateView):
    model = models.CustomUser
    template_name = 'user/user_update.html'
    form_class = forms.UserUpdateForm
 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('user_detail', kwargs={'pk': pk})
 
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
#  有料会員
class SubscribeRegisterView(View):
    template = 'subscribe/subscribe_register.html'
    
    def get(self, request):
        context = {}
        return render(self.request, self.template, context)
 
    def post(self, request):
        user_id = request.user.id
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
 
        correct_cord_number = '4242424242424242'
        if card_number != correct_cord_number:
            context = {'error_message': 'クレジットカード番号が正しくありません'}
            return render(self.request, self.template, context)
        
        models.CustomUser.objects.filter(id=user_id).update(is_subscribed=True,card_name=card_name,card_number=card_number)
        return redirect(reverse_lazy('top_page'))

class SubscribeCancelView(generic.TemplateView):
    template_name = 'subscribe/subscribe_cancel.html'

    def post(self, request):
        user_id = request.user.id

        models.CustomUser.objects.filter(id=user_id).update(is_subscribed=False)
        return redirect(reverse_lazy('top_page'))
    
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from . import models

class SubscribePaymentView(View):
    template = 'subscribe/subscribe_payment.html'

    def get(self, request):
        user_id = request.user.id
        user = models.CustomUser.objects.get(id=user_id)
        context = {'user': user}
        return render(request, self.template, context)

    def post(self, request):
        user_id = request.user.id
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        print(card_name, card_number)
        models.CustomUser.objects.filter(id=user_id).update(card_name=card_name, card_number=card_number)
        return redirect(reverse_lazy('top_page'))


# ユーザー管理
class ManagementUserListView(onlyManagementUserMixin, generic.ListView):
    template_name = "management/user_list.html"
    model = models.CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "user"
        
        return context
    
class ManagementUserListUpdateView(onlyManagementUserMixin, generic.UpdateView):
    template_name = "management/user_list_update.html"
    model = models.CustomUser

    form_class = forms.UserUpdateForm
 
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('user_detail', kwargs={'pk': pk})
 
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
#　カテゴリー
class ManagementCategoryListView(onlyManagementUserMixin, generic.ListView):
    template_name = "management/category_list.html"
    model = Category
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "category"
        
        return context
    
class ManagementCategoryCreateView(onlyManagementUserMixin, generic.CreateView):
    model = Category
    template_name = 'management/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "category"
        
        return context

# レストラン
class ManagementRestaurantListView(onlyManagementUserMixin, generic.ListView):
    template_name = "management/restaurant_manage_list.html"
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "restaurant"
        
        return context
    
class ManagementRestaurantCreateView(onlyManagementUserMixin, generic.CreateView):
    model = Restaurant
    template_name = 'management/restaurant_create.html'
    fields = '__all__'
    success_url = reverse_lazy('restaurant_manage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "restaurant"
        
        return context

class ManagementRestaurantUpdateView(onlyManagementUserMixin, generic.UpdateView):
    template_name = 'management/restaurant_update.html'
    form_class = forms.RestaurantUpdateForm
    model = Restaurant
    success_url = reverse_lazy('restaurant_manage_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["del_restaurant_id"] = self.request.path.split('/')[-2]
        context["selected"] = "restaurant"

        return context
    
class ManagementRestaurantDeleteView(onlyManagementUserMixin, generic.DeleteView):
    model = Restaurant
    template_name = 'management/restaurant_delete.html'
    success_url = reverse_lazy('restaurant_manage_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        del_restaurant_id = self.request.path.split('/')[-2]
        context["del_restaurant"] = Restaurant.objects.get(id=del_restaurant_id)
        context["selected"] = "restaurant"

        return context


# 売上
class ManagementSalesListView(onlyManagementUserMixin, generic.ListView):
    template_name = 'management/sales.html'
    model = Sales
    ordering = ["-year","-month"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["del_restaurant_id"] = self.request.path.split('/')[-2]
        context["selected"] = "restaurant"

        return context



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected"] = "sales"
        
        return context



