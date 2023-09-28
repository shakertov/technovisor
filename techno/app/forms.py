from django.contrib.auth import get_user_model
from django import forms
from app.models import DishModel


User = get_user_model()

USER_CHOICES = User.objects.values_list('id', 'username')
DISH_CHOICES = DishModel.objects.values_list('id', 'title')


class OrderForm(forms.Form):
	user = forms.ChoiceField(
		label='Пользователь',
		help_text='Выберите пользователя, которому необходим обед.',
		choices=USER_CHOICES)
	date = forms.DateField(
		label='Дата доставки',
		help_text='Введите дату доставки обеда в формате ГГГГ-ММ-ДД.')
	dishes = forms.MultipleChoiceField(
		label='Блюда',
		help_text='Выберите блюда для обеда.',
		widget=forms.SelectMultiple,
		choices=DISH_CHOICES)
	lucky = forms.BooleanField(
		label='Мне повезёт!',
		help_text='Хотите случайное блюдо?',
		required=False)


class DateForm(forms.Form):
	date = forms.DateField(
		label='Дата доставки',
		help_text='Введите дату для получения отчёта в формате ГГГГ-ММ-ДД.')
