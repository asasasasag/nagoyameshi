from django.contrib import admin
from .models import Category, Restaurant, Reservation, Review, Favorite, Sales

class SalesAdmin(admin.ModelAdmin):
    list_display = ("year","month","amount")

admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Sales, SalesAdmin)