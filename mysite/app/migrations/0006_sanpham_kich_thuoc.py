# Generated by Django 5.0.4 on 2024-05-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_diachigiaohang_khach_hang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='kich_thuoc',
            field=models.IntegerField(default=37, max_length=10),
        ),
    ]
