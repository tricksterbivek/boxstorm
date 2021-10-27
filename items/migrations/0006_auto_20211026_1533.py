# Generated by Django 3.2.8 on 2021-10-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20211026_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='unit_id',
            new_name='unit',
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
