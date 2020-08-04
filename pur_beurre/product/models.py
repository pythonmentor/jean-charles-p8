from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    stores = models.CharField(max_length=100)
    url = models.URLField()
    categories = models.ManyToManyField('Category', related_name='products')

    
    class Meta:
        verbose_name = "Produit"
        ordering = ['name']
    
    def __str__(self):
        """ 
        Cette méthode permet de definit l'entité product
        """
        return self.name



class Category(models.Model):
    tag = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    url = models.URLField()
#    products = models.ManyToManyField('product.Product')
# related_names
    
    class Meta:
        verbose_name = "Categorie"
        ordering = ['name']
    
    def __str__(self):
        """ 
        Cette méthode permet de definit l'entité category
        """
        return self.name