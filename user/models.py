from django.db import models
from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):

    CHOICES = (
        ("News", _('News')),
        ("Yangiliklar", _("Yangiliklar")),
        ("Articles", _('Articles')),
        ("Maqolalar", _("Maqolalar")),
        ("Books", _("Books")),
        ("Kitoblar", _("Kitoblar"))
    )

    my_choice = models.CharField(max_length=500, choices=CHOICES)

    def __str__(self):
        return self.my_choice

