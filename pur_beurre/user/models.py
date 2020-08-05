from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['first_name']

    def __str__(self):
        """ 
        Cette méthode permet d'afficher l'entité category
        """
        return self.first_name + ", " + self.last_name + ", " + str(self.status)
