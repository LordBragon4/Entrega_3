# Generated by Django 2.1.2 on 2018-11-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_misperris', '0008_auto_20181108_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
