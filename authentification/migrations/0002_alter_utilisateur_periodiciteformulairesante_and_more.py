# Generated by Django 4.2.5 on 2023-11-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='periodiciteFormulaireSante',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='periodiciteFormulaireStress',
            field=models.IntegerField(default=None, null=True),
        ),
    ]