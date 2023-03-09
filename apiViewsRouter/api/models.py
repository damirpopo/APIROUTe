from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=30)

    def __str__(self):
        return self.category

class TypeAnimal(models.Model):
    typeAnimal=models.CharField(max_length=30)

    def __str__(self):
        return self.typeAnimal

class Status(models.Model):
    status=models.CharField(max_length=30)

    def __str__(self):
        return self.status

class Name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Pet(models.Model):
    name=models.ForeignKey(Name,on_delete= models.CASCADE, null=True)
    foto=models.URLField()
    category=models.ForeignKey(Category,on_delete= models.CASCADE, null=True)
    typeAnimal=models.ForeignKey(TypeAnimal,on_delete= models.CASCADE, null=True)
    status=models.ForeignKey(Status,on_delete= models.CASCADE, null=True)

class Zakaz(models.Model):
    nameAnimal=models.ForeignKey(Name,on_delete= models.CASCADE, null=True)
    count=models.IntegerField()
    dataSale=models.DateTimeField()
    status=models.BooleanField(default=False,blank=True,null=True,)





