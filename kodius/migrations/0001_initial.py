# Generated by Django 4.0.5 on 2022-07-08 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('last_supported_year', models.IntegerField(null=True)),
                ('chain_change_price', models.FloatField(null=True)),
                ('oil_and_oil_filter_change_price', models.FloatField(null=True)),
                ('air_filter_change_price', models.FloatField(null=True)),
                ('brake_fluid_change_price', models.FloatField(null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kodius.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_year', models.IntegerField(null=True)),
                ('mileage', models.IntegerField(null=True)),
                ('choose_date', models.DateField(null=True)),
                ('chain_change_price', models.BooleanField(default=False, null=True)),
                ('oil_and_oil_filter_change_price', models.BooleanField(default=False, null=True)),
                ('air_filter_change_price', models.BooleanField(default=False, null=True)),
                ('brake_fluid_change_price', models.BooleanField(default=False, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kodius.brand')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kodius.model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
