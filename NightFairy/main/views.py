from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from array import *

from .models import Db, Rubric
from .forms import DbForm

class DbCreateView(CreateView):
	template_name = 'main/create.html'
	form_class = DbForm
	success_url = reverse_lazy('index')

	def get_context_date(self, **kwards):
		context = super().get_context_date(**kwards)
		context['rubrics'] = Rubric.objscts.all()

		return context

def delItem(request, product_id):
	sess = request.session['cart'].pop(str(product_id))
	request.session.modified = True


	return redirect('/main/cart/')
def by_rubric(request, rubric_id):
	dbs = Db.objects.filter(rubric=rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk = rubric_id)
	context = {'dbs':dbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
	return render(request, 'main/by_rubric.html', context)

def product(request, product_id):
	try:
		db = Db.objects.get(id = product_id)
		rubrics = Rubric.objects.all()
		context = {'db': db, 'rubrics': rubrics}

	except ObjectDoesNotExist:
		raise Http404

	return render(request, 'main/product.html',context)

def addToCart(request, product_id):
	form = request.POST
	args = []
	if 'cart' in request.session:
		sess = request.session.get('cart')
		if str(product_id) not in sess:
			title=Db.objects.get(id = product_id).title

			if Db.objects.get(id = product_id).on_stock:
				price=Db.objects.get(id = product_id).stock_price	
			else:
				price=Db.objects.get(id = product_id).price

			args.insert(0,title)
			args.insert(1,price)
			args.insert(2, int(form['number']))
			sess[str(product_id)] = args
			request.session.modified = True

		else:
			title=Db.objects.get(id = product_id).title

			if Db.objects.get(id = product_id).on_stock:
				price=Db.objects.get(id = product_id).stock_price	
			else:
				price=Db.objects.get(id = product_id).price

			args.insert(0,title)
			args.insert(1,price)
			args.insert(2, int(sess[str(product_id)][2]) + int(form['number']))
			sess[str(product_id)] = args
			request.session.modified = True
			
	else:
		title=Db.objects.get(id = product_id).title

		if Db.objects.get(id = product_id).on_stock:
			price=Db.objects.get(id = product_id).stock_price
			
		else:
			price=Db.objects.get(id = product_id).price

		args.insert(0,title)
		args.insert(1,price)
		args.insert(2,int(form['number']))
		request.session.set_expiry(9999999) # от бaлды
		request.session['cart'] = { str(product_id) : args }
		request.session.modified = True
	print(str(request.session['cart']))

	return redirect('/main/cart') 

def index(request):
	dbs = Db.objects.order_by('-published')
	rubrics = Rubric.objects.all()	
	context = {'dbs': dbs, 'rubrics': rubrics}
	return render(request, 'main/index.html', context)
def stocks(request):
	dbs = Db.objects.filter(on_stock = True)
	rubrics = Rubric.objects.all()
	context = {'dbs': dbs, 'rubrics': rubrics}
	return render(request, 'main/stocks.html', context)
def about_us(request):
	rubrics = Rubric.objects.all()
	context = {'rubrics': rubrics}
	return render(request, 'main/about_us.html', context)
def basket(request):
	rubrics = Rubric.objects.all()
	context = {'rubrics': rubrics}
	return render(request, 'main/basket.html', context)
def cart(request):
	rubrics = Rubric.objects.all()
	dbs = Db.objects.all()
	try:
		sess = request.session['cart']
		isCart = True
	except:

		sess = ''
		isCart = False
		Id = []
		title = []
		price = []
		number = []
		totalPrice = 0
	if len(sess) == 0:
		isCart = False

	Id = []
	title = []
	price = []
	number = []
	LPrice = []
	nI = 0
	nT = 0
	nP = 0
	nN = 0
	nPL = 0
	totalPrice = 0
	for i in sess:
		Id.insert(nI,i)
		nI += 1

	for i in sess:
		title.insert(nT,str( sess[str(i)][0] ))
		nT += 1

	for i in sess:
		price.insert(nP,str( sess[str(i)][1] ))
		nP += 1

	for i in sess:
		number.insert(nN,str( sess[str(i)][2] ))
		nN += 1

	for i in price:
		LPrice.insert(nPL, str(float(i) * int(number[nPL])))
		nPL +=1

	FPrice = price



	for i in LPrice:
		totalPrice += float(i)

	context = {'isCart':isCart ,'totalPrice':totalPrice, 'rubrics': rubrics, 'sess':sess, 'dbs':dbs, 'Id':Id, 'title':title, 'FPrice':FPrice, 'LPrice':LPrice, 'number': number}
	return render(request, 'main/cart.html', context)

def plusNumber(request, product_id):
	form = request.POST
	sess = request.session['cart']

	sess[str(form['plus'])].insert(2, int(sess[str(form['plus'])][2]) + 1) 
	request.session.modified = True

	return redirect('/main/cart/')

def minusNumber(request, product_id):
	form = request.POST
	sess = request.session['cart']
	num = int(sess[str(form['minus'])][2]) - 1
	if num <= 0:
		delItem(request, product_id)
	else:

		sess[str(form['minus'])].insert(2,num ) 
		request.session.modified = True

	return redirect('/main/cart/')
def pay(request):
	rubrics = Rubric.objects.all()
	context = {'rubrics': rubrics}
	
	return render(request, 'main/pay.html', context)