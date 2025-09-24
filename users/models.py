from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True, 
                              error_messages={"unique": _("Um usuário com este email já está cadastrado.")})

    id = models.CharField(_("matricula"), 
        max_length=13,
        unique=True, 
        primary_key=True,
        help_text=_(
            "Seu número de matrícula do SUAP ou SIAPE. Apenas números."
        ),
        error_messages={
            "unique": _("Um usuário com este número de matrícula já está cadastrado.")
        }
    )

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    objects = CustomUserManager()

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.id.isdigit():
            raise ValidationError("O campo da matrícula pode conter apenas números.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"


class Card(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='card')
    card_number = models.CharField(_("Número do Cartão"), max_length=20, unique=True)

    def __str__(self):
        return f'Cartão {self.card_number} - {self.user.first_name} {self.user.last_name}'


class RegistrationRequest(models.Model):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"))
    id_number = models.CharField(_("matricula"), max_length=13)
    password = models.CharField(_("password"), max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('approved', 'Aprovado'),
        ('rejected', 'Rejeitado'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_number}) - {self.get_status_display()}"
