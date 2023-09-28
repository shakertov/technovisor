from django.contrib import admin


from app.models import DishModel, OrderModel, OrderDishModel

admin.site.register(DishModel)
admin.site.register(OrderModel)
admin.site.register(OrderDishModel)
