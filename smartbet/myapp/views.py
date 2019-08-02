from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from requests import get
from bs4 import BeautifulSoup
from .models import *

# Create your views here.
def scrap(request):
   url = 'https://www.matchendirect.fr/'
   response = get(url)
   html_soup = BeautifulSoup(response.text, 'html.parser')

   table = html_soup.find('div', attrs={'id': 'livescore'})
   compt = 1

   mydata = []

   for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

       a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

       for el in row.findAll('tr'):
         resultat = {}
         heure = el.find('td', attrs={'class': 'lm1'}).get_text()
         eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
         eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()

         scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

         resultat['heure'] = heure
         resultat['eqa'] = eqA
         resultat['eqb'] = eqB
         resultat['scors'] = scors

         mydata.append(resultat)
   data = mydata

   return JsonResponse(data, safe=False)  # retourn du json


def index(request):
    return render(request, 'myapp/index.html')

def pari(request):
    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs={'id': 'livescore'})
    compt = 1

    mydata = []

    for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

        a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

        for el in row.findAll('tr') :
            resultat = {}
            heure = el.find('td', attrs={'class': 'lm1'}).get_text()
            eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
            eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()
            scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

            resultat['heure'] = heure
            resultat['eqa'] = eqA
            resultat['eqb'] = eqB
            resultat['scors'] = scors

            mydata.append(resultat)

        data = mydata
        send = { 'resultat': data
        }
        return render(request, 'myapp/pari.html', send)

def form(request):
    return render(request, 'myapp/form.html')

def register(request):
    userName=request.POST.get('username', False)
    password=request.POST.get('password', False)
    try:
        user=User(username = userName)
        user.save()
        user.password=password
        user.set_password(user.password)
        user.save()

        print(userName, password)
    except:
        print("Veuillez remplir le formulaire svp")
    return render(request, 'myapp/form.html')

def connexion(request):
    return render(request, 'myapp/connexion.html')
@login_required(login_url='/login')
def resultat(request):
    return render(request, 'myapp/resultat.html')

def mylogin(request):
    userName = request.POST.get('username', False)
    password =  request.POST.get('password', False)
    user = authenticate(username = userName, password = password)
    if user is not None:
        login(request, user)
        return redirect('resultat')
    else:
        return redirect('connexion')
def mylogout(request):
    logout(request)
    return redirect('index')




