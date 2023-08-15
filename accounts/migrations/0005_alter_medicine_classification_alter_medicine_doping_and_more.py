# Generated by Django 4.2.4 on 2023-08-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_medicine_ingredients_amount_medicine_classification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='classification',
            field=models.TextField(default='', null=True, verbose_name='medi_classification'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='doping',
            field=models.TextField(default='', null=True, verbose_name='doping'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='efficacy',
            field=models.TextField(null=True, verbose_name='efficacy'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.TextField(default='', null=True, verbose_name='medicine_name'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='storage',
            field=models.TextField(default='', null=True, verbose_name='storage'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='usage',
            field=models.TextField(default='', null=True, verbose_name='usage'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='warning',
            field=models.TextField(default='', null=True, verbose_name='warning'),
        ),
    ]
