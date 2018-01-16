# Generated by Django 2.0.1 on 2018-01-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.IntegerField(default=8000000, primary_key=True, serialize=False)),
                ('drawing_number', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_choice', models.CharField(choices=[('ORDER', 'Order'), ('SAMPLE', 'Sample')], default='ORDER', max_length=20)),
                ('order_by', models.CharField(max_length=50, null=True)),
                ('post_date', models.DateTimeField(verbose_name='date posted')),
                ('requested_date', models.DateTimeField(verbose_name='request date')),
                ('status', models.CharField(choices=[('QUEUE', 'Queue'), ('WIP', 'Wip'), ('COMPLETE', 'Complete'), ('HOLD', 'Hold')], default='QUEUE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='request_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Request'),
        ),
    ]
