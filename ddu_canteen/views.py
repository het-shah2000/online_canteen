from typing import ItemsView
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.db.models import F
from django.http import JsonResponse
import json
import requests
import random

def home(request):
    order, created = Order.objects.get_or_create(complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    content = {
        'items': Item.objects.all(),
        'item':items, 'order':order,
        'cartItems':cartItems
    }
    return render(request, 'ddu_canteen/home.html' , content)

def register(request):
    if request.method == "POST":
        print("Registered")
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        id = request.POST['college_id']
        p1 = request.POST['pass']
        p2 = request.POST['re-pass']
        email = request.POST['email']
        phone = request.POST['phone']
        p = str(phone)
        fn = str(firstname)

        # user = User(username = username, first_name=firstname, last_name=lastname, email = email, password = p1)
        # user.save()
        # student = Student(user = user, college_id=id)
        # student.save()

        url = "https://www.fast2sms.com/dev/bulk"
        # querystring = {"authorization":"Tf0l5vJFUNs3EqRDwmVpjkIHLbYXSBtxGicuhyPQdW9nr2e178brnxh0MUt2DmlTGoPKJLEvaAYN9SW6","sender_id":"TXTIND","message":"Welcome","route":"dlt","numbers":p}

        # headers = {
        #     'cache-control': "no-cache"
        # }

        # response = requests.request("GET", url, headers=headers, params=querystring)
        otp = random.randint(1000,9999)
        o = str(otp)
        # print(response.text) 
        my_data = { 
            # Your default Sender ID 
            'sender_id': 'TXTIND',  
            
            # Put your message here! 
            'message': 'Welcome to bunkORNER, '+fn+ ' Your OTP is '+ o,  
            
            'language': 'english', 
            'route': 'p', 
            
            # You can send sms to multiple numbers 
            # separated by comma. 
            'numbers': p    
        }
        headers = { 
            'authorization': 'Tf0l5vJFUNs3EqRDwmVpjkIHLbYXSBtxGicuhyPQdW9nr2e178brnxh0MUt2DmlTGoPKJLEvaAYN9SW6', 
            'Content-Type': "application/x-www-form-urlencoded", 
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", 
                            url, 
                            data = my_data, 
                            headers = headers)
        print(response)
        return redirect('/')
    else:
        return render(request, 'ddu_canteen/register.html')


def login(request):
    return render(request, 'ddu_canteen/login.html')

def cart(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     student = Student.objects.get(user=F('user'))
    #     print(student)
    #     order, created = Order.objects.get_or_create(student=student, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    #     items = []
    user = request.user
    order, created = Order.objects.get_or_create(complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'ddu_canteen/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    action = data['action']
    print('Action:', action)
    print('ItemId:', itemId)

    user = request.user
    item = Item.objects.get(id=itemId)
    # student = Student.objects.get(user=user)
    order, created = Order.objects.get_or_create(complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item = item)
    if(action == 'add'):
        orderItem.quantity = (orderItem.quantity + 1)
    elif(action == 'remove'):
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity < 0:
        orderItem.delete()
    return JsonResponse('Item was Added', safe=False)






        # email_subject = 'Activate your Account'
        # email_body =  'Click on the link to activate your bunkORNER account'
        # email = EmailMessage(
        #     email_subject,
        #     email_body,
        #     'noreply@tehhet.com',
        #     [email],
            
        # )
        # send_mail(
        #     email_subject,
        #     email_body,
        #     'tyewatson0@gmail.com',
        #     ['gautamrizwani@gmail.com', email],
        #     fail_silently=False
        # )
        # mail = EmailMessage(
        #     email_subject,
        #     email_body,
        #     'tyewatson0@gmail.com',
        #     ['gautamrizwant@gmail.com', email]
        # )
        # mail.send(fail_silently=False)

    """def registration_done(request):
    if request.method == "POST":
        print("Registered")
        name = request.POST['name']
        id = request.POST['college_id']
        p1 = request.POST['pass']
        p2 = request.POST['re-pass']
        email = request.POST['email']

        info = Student(name=name, college_id=id, password=p1, email=email)
        info.save()
        return redirect("ddu_canteen/home.html")
    else:
        print("No request")"""