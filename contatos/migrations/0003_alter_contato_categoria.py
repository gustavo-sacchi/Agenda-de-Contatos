# Generated by Django 3.2.7 on 2021-10-06 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20211005_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='categoria',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria'),
        ),
    ]
