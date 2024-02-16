from django.db import models

class Db(models.Model):
	title = models.CharField(max_length = 50, verbose_name = 'Название')
	content = models.TextField(null = True, blank = True, verbose_name = 'Краткое описание')
	full_content = models.TextField(null = True, blank = True, verbose_name = 'Полное Описание')
	price = models.FloatField(null = True, blank  = True, verbose_name = 'Цена')
	published = models.DateField(auto_now_add = True, db_index = True, verbose_name = 'Опубликовано')
	img_name = models.CharField(max_length = 100, verbose_name = 'Путь к изображению(src/photo.png)')
	rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = 'Рубрика')
	on_stock =models.BooleanField(default = False, blank = False, verbose_name = 'Есть ли акция?')
	stock_price = models.FloatField(null = True, blank  = True, verbose_name = 'Цена по акции')

	class Meta:
		verbose_name_plural = 'Обьявления'
		verbose_name = 'Обьявление'
		ordering = ['-published']
		
class Rubric(models.Model):
	name = models.CharField(max_length = 50, db_index = True, verbose_name = 'Название')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'
		ordering = ['name']

