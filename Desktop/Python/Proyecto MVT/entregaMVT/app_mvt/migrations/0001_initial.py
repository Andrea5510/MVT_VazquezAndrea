# Generated by Django 4.0.3 on 2022-03-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('cantidad_hijos', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]