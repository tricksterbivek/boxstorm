# Generated by Django 3.2.8 on 2021-10-26 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_category_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.unit'),
        ),
    ]