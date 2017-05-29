from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	cod = models.AutoField(primary_key=True)
	provider = models.OneToOneField('Provider', on_delete=models.CASCADE)
	name = models.CharField(max_length=255, blank=True, null=False, verbose_name='Nome')
	in_stock = models.IntegerField()
	price_sale = models.DecimalField(max_digits=12, decimal_places=6, verbose_name='Preço de venda')
	price_cost = models.DecimalField(max_digits=12, decimal_places=6, verbose_name='Preço de custo')

	def get_profit(self):
		return self.price_sale / self.price_cost 

class Sale_Unit(models.Model):
	cod = models.AutoField(primary_key=True)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)
	name = models.CharField(max_length=55, blank=True) #This should be a choice list, maybe another model
	amount = models.IntegerField()
	price_mult = models.DecimalField(max_digits=8, decimal_places=6, default=1, verbose_name='Incremento de preço')

class Customer(models.Model):
	cod = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=155, blank=True, null=False, verbose_name='Endereço')
	person_type = models.CharField(max_length=55, blank=False, null=False, default='Pessoa Física')
	document = models.IntegerField(verbose_name='Núm. Documento')

class Provider(models.Model):
	cod = models.AutoField(primary_key=True)
	address = models.CharField(max_length=155, blank=True, null=False, verbose_name='Endereço')
	person_type = models.CharField(max_length=55, blank=False, null=False, default='Pessoa Física')
	document = models.IntegerField(verbose_name='Núm. Documento')

class Sale(models.Model):
	cod = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product, through='Sale_Item')
	date_created = models.DateField()
	date_closed = models.DateField()
	status = models.CharField(max_length=55, blank=False, null=False, default='Em aberto', verbose_name='Status')

class Sale_Item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
	quantity = models.IntegerField()
