from django.db import models

class CategoryChoices(models.Model):
  category_name = models.CharField(max_length=100)
  def __str__(self):
        return self.category_name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=True,blank=True,default=0)
    category = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    def __str__(self):
        return self.name

class CookingName(models.Model):
  cooking_name = models.CharField(max_length=100)
  category = models.ForeignKey(CategoryChoices,on_delete=models.PROTECT)
  tags = models.ManyToManyField(Tag, blank=True)
  images = models.ImageField(upload_to='')
  count = models.IntegerField(null=True,blank=True,default=0)
  how = models.TextField(blank=True)
  
  def __str__(self):
        return self.cooking_name

# class CuisineModel(models.Model):
