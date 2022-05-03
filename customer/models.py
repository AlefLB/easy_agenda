from django.db import models

from users.models import User


class Customer(models.Model):
    GENDER_OPTIONS = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
        ('o', 'Outros'),
    )
    
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    postal_code = models.CharField(max_length=8)
    address = models.CharField(max_length=150)
    address_number = models.CharField(max_length=7)
    complement = models.CharField(max_length=70, null=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    tel1 = models.CharField(max_length=11)
    tel2 = models.CharField(max_length=11, null=True)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='customer')
    creator = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='customer_creator_set')
    updater = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='customer_updater_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
