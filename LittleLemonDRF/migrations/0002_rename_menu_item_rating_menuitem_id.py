# Generated by Django 4.2.7 on 2024-02-29 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='menu_item',
            new_name='menuitem_id',
        ),
    ]