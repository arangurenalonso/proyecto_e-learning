# Generated by Django 3.1.7 on 2021-03-29 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='code_paypal',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='quantity',
        ),
    ]