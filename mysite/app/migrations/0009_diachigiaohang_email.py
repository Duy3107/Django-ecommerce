# Generated by Django 5.0.4 on 2024-05-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_diachigiaohang_phuong'),
    ]

    operations = [
        migrations.AddField(
            model_name='diachigiaohang',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
    ]
