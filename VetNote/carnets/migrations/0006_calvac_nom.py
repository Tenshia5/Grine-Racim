# Generated by Django 4.0.4 on 2022-05-24 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carnets', '0005_alter_consultation_poids_cons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calvac',
            name='nom',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='carnets.carnet'),
            preserve_default=False,
        ),
    ]
