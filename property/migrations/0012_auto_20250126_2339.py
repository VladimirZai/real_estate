# Generated by Django 3.2 on 2025-01-26 22:39

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_rename_owner_flat_owner_deprecated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='owners_phonenumber',
        ),
        migrations.AddField(
            model_name='owner',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Номер владельца'),
        ),
    ]
