from django.db.models import fields
from django.forms import ModelForm
from .models import *
class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['Libellé','Description'] #pour quelques champs

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"

    