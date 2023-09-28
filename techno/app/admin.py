from django.contrib import admin
from app.models import DishModel, OrderModel, OrderDishModel


@admin.register(DishModel)
class DishAdmin(admin.ModelAdmin):
	list_display = ('title', 'ingredients', 'price')


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('date', 'display_user', 'user')
	list_filter = ('date', )

	def display_user(self, obj):
		return ' '.join([obj.user.first_name, obj.user.last_name])

	display_user.short_description = 'ФИО'


@admin.register(OrderDishModel)
class OrderDishAdmin(admin.ModelAdmin):
	list_display = ('order', 'dish')
	list_filter = ('dish', )
