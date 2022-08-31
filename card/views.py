from email.headerregistry import Address
from traceback import print_tb
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import invcard, contact, team, faq, offer
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def index(request):
    allcart= []
    cats= invcard.objects.values('category', 'code')
    cat= {item['category'] for item in cats}
    for i in cat:
        cards= invcard.objects.filter(category= i)
        allcart.append(cards)
    teams= team.objects.all()
    offers=offer.objects.all().first   
    params= {'allcart': allcart,
              'teams' : teams,
              'offers': offers
                 }
    return render(request, 'card/index.html', params)

def cart(request):
    allcart= []
    cats= invcard.objects.values('category', 'code')
    cat= {item['category'] for item in cats}
    for i in cat:
        cards= invcard.objects.filter(category= i)
        allcart.append(cards)
    params= {'allcart': allcart}
    return render(request, 'card/card1.html', params)


def viewcard(request, slug):
    viewcards= invcard.objects.filter(code= slug)[0]
    print(viewcards)
    return redirect("cart", {"viewcardss": viewcards})


def contact_us(request):
    if(request.method=='POST'):
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        number= request.POST.get('number', '')
        address= request.POST.get('address', '')
        desc= request.POST.get('desc', '')
        msg= 'Name: '+ name + '\n' + 'Email: '+ email + '\n' +'Number: '+ number + '\n' + 'Address: '+ address + '\n' + 'Message: '+ desc
        contacts= contact(name=name, email= email, number=number, address=address, desc=desc)
        contacts.save()
        send_mail(name, msg, 'arvind.mandloi04@gmail.com', ['arvind.mandloi04@gmail.com'], fail_silently=False,)
        thank=True
        messages.success(request, "Thanks for Contact us")
        return render(request, "card/contact.html", {"thank":thank})
    return render(request, "card/contact.html")

def faqs(request):
    fa= faq.objects.all()
    return render(request, 'card/faq.html', {'fa' : fa})  
