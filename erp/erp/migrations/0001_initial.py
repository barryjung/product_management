# Generated by Django 4.2 on 2023-04-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('price', models.CharField(max_length=256)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('F', 'Free')], max_length=1)),
                ('inbound_quantity', models.IntegerField(default=0)),
                ('outbound_quantity', models.IntegerField(default=0)),
                ('stock_quantity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ammount', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
            options={
                'db_table': 'outbound',
            },
        ),
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_inbound_quantity', models.IntegerField()),
                ('total_inbound_ammount', models.IntegerField()),
                ('total_outbound_quantity', models.IntegerField()),
                ('total_outbound_ammount', models.IntegerField()),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='erp.product')),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ammount', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
            options={
                'db_table': 'inbound',
            },
        ),
    ]