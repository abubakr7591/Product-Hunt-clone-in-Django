from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
	products = Product.objects
	return render(request, 'prodects/home.html',{'products':products})

@login_required(login_url="/accounts/signup")
def product_create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] and request.POST['body_content']:
			product = Product()
			product.title = request.POST['title']
			product.url = request.POST['url']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.body = request.POST['body_content']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/products/' + str(product.id))
		else:
			return render(request, 'prodects/product_create.html',{'error': 'All fields are required'})		
	else:
		return render(request, 'prodects/product_create.html')


def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'prodects/detail.html', {'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect('/products/' + str(product.id))
