# Generated by Django 3.2.7 on 2021-10-06 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_alter_contato_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria'),
        ),
    ]
