from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Sum, F, Value, FloatField
from app.forms import OrderForm, DateForm
from app.models import OrderModel, OrderDishModel, DishModel
import random


def order(request):
	form = OrderForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			# Создать запись заказа
			order, state = OrderModel.objects.get_or_create(
				user_id=form.cleaned_data['user'],
				date=form.cleaned_data['date'])
			# Случайное блюдо
			if form.cleaned_data.get('lucky') == True:
				dish = DishModel.objects.order_by('?').first()
				form.cleaned_data['dishes'].append(dish.id)
				messages.info(request, 'Вам случайным образом добавлено блюдо: ' + dish.title)
			# Создать блюда к заказу
			menu = OrderDishModel.objects.bulk_create([
				OrderDishModel(order=order, dish_id=d) for d in form.cleaned_data['dishes']])
			messages.info(request, 'Блюда добавлены на доставку к выбранному пользователю!')
			return redirect('order')
	data = {
		'title': 'Страница для заказа',
		'form': form
	}
	return render(request, 'order.html', data)


def my_orders(request):
	if request.user.is_authenticated:
		orders = OrderModel.objects.filter(user=request.user)

		obj_per_page = 1
		orders = Paginator(orders, obj_per_page)
		page_number = request.GET.get('page')
		orders = orders.get_page(page_number)

		data = {
			'title': 'Мои заказы',
			'orders': orders
		}
		return render(request, 'my-orders.html', data)

	return render(request, 'not_auth.html')


def date(request):
	form = DateForm(request.POST or None)
	data = {
		'title': 'Отчёт на дату',
		'form': form
	}
	if request.method == 'POST':
		if form.is_valid():
			date = form.cleaned_data['date']
			total_dishes = DishModel.objects.filter(
				list__order__date=date).annotate(
				dish_count=Count('id'),
				sum=F('price') * F('dish_count'),
				totals=Value(DishModel.objects.filter(
					list__order__date=date).aggregate(Sum('price'))['price__sum'], FloatField()))
			data['total_dishes'] = total_dishes
			if total_dishes:
				messages.info(request, 'Отчёт сформирован!')
			else:
				messages.info(request, 'В выбранную дату не было заказов!')
	return render(request, 'date.html', data)

