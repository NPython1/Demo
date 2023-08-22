from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="category",blank=True)

    class Meta:
        ordering=("name",)
        verbose_name="Category"
        verbose_name_plural="Categories"

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shop:products_by_category',args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product", blank=True)
    available=models.BooleanField(default=True)
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:ProdCatdetail',args=[self.category.slug, self.slug])

    class Meta:
        ordering = ("name",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return '{}'.format(self.name)


