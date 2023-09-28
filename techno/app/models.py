from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DishModel(models.Model):
	title = models.CharField(max_length=32, verbose_name='Название')
	ingredients = models.CharField(max_length=100, verbose_name='Ингредиенты')
	price = models.FloatField(verbose_name='Цена за единицу')

	class Meta:
		verbose_name = 'Блюдо'
		verbose_name_plural = 'Блюд(о-а)'

	def __str__(self):
		return self.title


class OrderModel(models.Model):
	date = models.DateField('Дата')
	user = models.ForeignKey(User, models.CASCADE, 'orders', verbose_name='Пользователь')

	class Meta:
		ordering = ['-date']
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы(ов)'

	def __str__(self):
		return 'Заказ на дату: ' + str(self.date)


class OrderDishModel(models.Model):
	order = models.ForeignKey(OrderModel, models.CASCADE, 'list', verbose_name='Заказ')
	dish = models.ForeignKey(DishModel, models.CASCADE, 'list', verbose_name='Блюдо')

	class Meta:
		verbose_name = 'Меню пользователя'
		verbose_name_plural = 'Меню пользователя'
