# Generated by Django 2.1.2 on 2018-11-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_misperris', '0010_auto_20181108_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='vivienda',
            field=models.CharField(max_length=20, null=True),
        ),
    ]