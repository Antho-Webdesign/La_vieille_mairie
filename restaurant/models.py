from django.db import models
from django.utils.text import slugify

TVA_1 = 0.1  # TVA de 10%
TVA_2 = 0.2  # TVA de 20%


class CategorieMenu(models.Model):
    nom = models.CharField(max_length=100)
    img_cat = models.ImageField(upload_to='images/categories', null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(CategorieMenu, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom


class ElementMenu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    img_item = models.ImageField(upload_to='images/items', null=True, blank=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ForeignKey(CategorieMenu, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, editable=False)
    tva_choice = models.CharField(max_length=5, default=TVA_1, choices=[(TVA_1, 'TVA 10%'), (TVA_2, 'TVA 20%')])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(ElementMenu, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom
