from django.db import models

class Item(models.Model):
    added_list  = models.TextField(max_length = 2050)

    def __str__(self):
        return self.added_list  