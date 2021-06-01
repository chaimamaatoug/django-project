from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import Commande, Fournisseur, Produit
from .forms import *
from django.shortcuts import redirect
# Create your views here.
def index(request): 
    list=Produit.objects.all()
    return render(request,'vitrine.html',{'list':list})


def addproduit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = ProduitForm()
        return render(request,'majProduits.html',{'form':form})

def viewfor(request):
    foni = Fournisseur.objects.all()
    return render(request,'viewforni.html',{'forni':foni})

def viewcommande(request):
    comm = Commande.objects.all()
    return render(request,'viewcommande.html',{'comm':comm})

def addcommande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('viewcomamnde')
    else:
        form = CommandeForm()
        return render(request,'addcommande.html',{'form':form})
