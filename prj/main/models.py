from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=300)
    difficulty = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    nutriention table =  
    cuisine = models.ForeignKey("Cuisine", on_delete=models.SET_NULL, null=True)
    


    def __str__(self):
        return f"Recipe <{self.name}> {self.year}"
        return f"Cuisine <{self.name}>"

class Cuisine(models.Model):
    name = models.CharField(max_length=300)