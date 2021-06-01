from django.db import models
from datetime import date
class Produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),
    ('fr','Frais'),
    ('cs','Conserve'),
    ]
    Libellé = models.CharField(max_length=100)
    Description = models.TextField(default='Non définie')
    Prix = models.DecimalField(max_digits=10,decimal_places=3)
    Type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img= models.ImageField(blank=True)
    Emballag = models.OneToOneField('Emballage',on_delete=models.CASCADE,null=True)
    fournisseur = models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return (" Libelllé : {}  Description: {}  Prix: {}  Type: {} Image: {} ").format(self.Libellé,self.Description,self.Prix,self.Type,self.img)



class Emballage(models.Model):
    COUL_CHOICES=[('bl','blanc'),
    ('rg','rouge'),
    ('ble','bleur'),
    ('vr','vert'),
    ('muli','multicolore')]
    Matiere = models.CharField( max_length=100 )
    Couleur = models.CharField( max_length=10,choices=COUL_CHOICES,default='Transparent')
    def __str__(self):
        return ("Matiere : "+self.Matiere + "Couleur :"+self.Couleur)

class Fournisseur(models.Model):
    Nom = models.CharField(max_length=100)
    Adresse = models.TextField(null=True)
    Email = models.EmailField(null=True)
    Telephone = models.CharField(max_length=8)
    def __str__(self):
        return ("Nom : {} Adresse : {} Email : {} Telephone : {} ").format(self.Nom,self.Adresse,self.Email,self.Telephone)

class ProduitNC(Produit,models.Model):
    Duree_garantie = models.CharField(max_length=100)
    def __str__(self):
        return (" Libelllé : {}  Description: {}  Prix: {}  Type: {} Image: {} Durée garantie : {} ").format(self.Libellé,self.Description,self.Prix,self.Type,self.img ,self.Duree_garantie)

class Commande(models.Model):
    Duree_garantie = models.CharField(max_length=100)
    dateCde = models.DateField(null=True,default=date.today)
    totalCde = models.DecimalField(max_digits=10,decimal_places=3)
    produits = models.ManyToManyField('Produit')
    def __str__(self):
        return ("duree garantie : {} date Cde : {} totalcde: {} ").format(self.Duree_garantie,self.dateCde,self.totalCde)






