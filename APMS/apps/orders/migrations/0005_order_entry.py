# Generated by Django 2.0.1 on 2018-01-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='entry',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='orders.Entry'),
        ),
    ]
