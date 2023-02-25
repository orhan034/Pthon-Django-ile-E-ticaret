from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    def __str__(self):
        return self.title
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategory"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Ürün Adı"), max_length=50)
    marka = models.CharField(("Marka"), max_length=50,null=True)
    text = models.TextField(("Açıklama"), max_length=700)
    image = models.FileField(("Fotograf"), upload_to='', max_length=100)
    fiyat = models.FloatField(("Fiyat"), default=0)
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    star = models.FloatField(("Beğeni"), default=0)
    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE,null=True)
    user = models.CharField(("Yorumu Yapan"), max_length=50, null=True)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"),max_length=1000)
    date_now = models.DateTimeField(("Tarih"), auto_now_add=True)
    like = models.IntegerField(("Beğeni"),default=0)
    def __str__(self):
        return self.title