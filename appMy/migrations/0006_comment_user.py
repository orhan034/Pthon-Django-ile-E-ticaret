# Generated by Django 4.1.5 on 2023-02-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=50, null=True, verbose_name='Yorumu Yapan'),
        ),
    ]
