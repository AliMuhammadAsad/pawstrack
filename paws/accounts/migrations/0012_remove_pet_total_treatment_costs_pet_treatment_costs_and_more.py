# Generated by Django 5.0.4 on 2024-04-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_pet_treatment_costs_pet_total_treatment_costs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='total_treatment_costs',
        ),
        migrations.AddField(
            model_name='pet',
            name='treatment_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='MedicalRecord',
        ),
    ]
