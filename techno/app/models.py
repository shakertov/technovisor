from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DishModel(models.Model):
	title = models.CharField(max_length=32)
	ingredients = models.CharField(max_length=100)
	price = models.FloatField()


class OrderModel(models.Model):
	date = models.DateField()
	user = models.ForeignKey(User, models.CASCADE, 'orders')

	class Meta:
		ordering = ['-date']


class OrderDishModel(models.Model):
	order = models.ForeignKey(OrderModel, models.CASCADE, 'list')
	dish = models.ForeignKey(DishModel, models.CASCADE, 'list')
