from django.db import models
from django.urls import reverse
from django.utils.text import slugify

TVA_1 = 0.1
TVA_2 = 0.2


class CategorieMenu(models.Model):
    nom = models.CharField(max_length=100)
    img_cat = models.ImageField(upload_to='images/categories', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(CategorieMenu, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    # Metadata
    class Meta:
        ordering = ['nom']
        verbose_name_plural = 'CategoriesMenu'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('categorie', args=[str(self.id)])


class ElementMenu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    img_item = models.ImageField(upload_to='images/items', null=True, blank=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ForeignKey(CategorieMenu, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, editable=False)
    tva_choice = models.CharField(max_length=5, default='0.1', choices=[('0.1', '10%'), ('0.2', '20%')])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(ElementMenu, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['nom']
        verbose_name_plural = 'ElementsMenu'


'''
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
        

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    nombre_personnes = models.IntegerField()

    def __str__(self):
        return f"{self.client.nom} - {self.date} {self.heure}"
        

class Menu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.reservation.client.nom} - {self.menu.nom} ({self.quantite})"


class Commande(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservation.client.nom} - {self.menu.nom} ({self.quantite})"


'''