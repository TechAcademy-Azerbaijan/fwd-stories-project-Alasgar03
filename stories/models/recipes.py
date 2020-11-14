from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    short_dscrp = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,db_index=True,related_name='recipe')

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
 