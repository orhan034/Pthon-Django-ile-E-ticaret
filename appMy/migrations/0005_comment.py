# Generated by Django 4.1.5 on 2023-02-25 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_product_marka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Yorum Başlığı')),
                ('text', models.TextField(max_length=1000, verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('like', models.IntegerField(default=0, verbose_name='Beğeni')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
            ],
        ),
    ]
