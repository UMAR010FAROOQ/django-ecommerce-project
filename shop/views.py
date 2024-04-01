from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Checkout, OrderUpdate
from math import ceil
import json


def login(request):
	if 'user_id' in request.session:
		text = "welcome " + request.session.get('user_id')
		context = {'message': text}
		return render(request, 'shop/index.html', context)

	if request.method == "POST":
		userID = request.POST.get("uname")
		passward = request.POST.get("psw")
		if userID == "admin" and passward == "123":
			request.session['user_id'] = userID
			text = "welcome to " + userID
			data = {'message': text, 'test' : "123"}
			return render(request, 'shop/index.html', data)
			
		else:
			context = {'message': 'Invalid credentials'}
			return render(request, 'shop/login.html', context =  context)
	else:
		return render(request, 'shop/login.html')


def index(request):
    if 'user_id' in request.session:
        allProds = []
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
        params = {'allProds': allProds}
        return render(request, "shop/index.html", params)
    else:
        return render(request, 'shop/login.html')
         


def logout(request):
	if 'user_id' in request.session:
		del request.session['user_id']

		return render(request, 'shop/login.html')
	else:
		return render(request, 'shop/login.html')
    


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = Contact(name=name, email=email, phone=phone, message=message)
        data.save()
    return render(request, "shop/contact.html")



def about(request):
    return render(request, "shop/about.html")



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Checkout.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')      

    return render(request, "shop/tracker.html")




def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html", {'product': product[0]})



def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        data = Checkout(items_json=items_json, amount=amount, name=name, email=email, address=address,city=city,
                       state=state,zip_code=zip_code,
                         phone=phone)
        data.save()
        update = OrderUpdate(order_id=data.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id1 = data.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id1})
    return render(request, 'shop/checkout.html')

