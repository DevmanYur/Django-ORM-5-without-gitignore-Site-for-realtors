# Generated by Django 3.2.21 on 2024-01-17 08:46

from django.db import migrations


def load_owned_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner, _ = Owner.objects.get_or_create(fullname=flat.owner, owners_phonenumber = flat.owners_phonenumber,
                                               owner_pure_phone = flat.owner_pure_phone)
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_claim_description'),
    ]

    operations = [migrations.RunPython(load_owned_flats),
    ]
