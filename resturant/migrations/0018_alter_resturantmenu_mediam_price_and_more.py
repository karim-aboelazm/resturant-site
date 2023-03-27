# Generated by Django 4.1.7 on 2023-03-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "resturant",
            "0017_resturantmenu_mediam_price_resturantmenu_small_price_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="resturantmenu",
            name="mediam_price",
            field=models.DecimalField(
                decimal_places=3,
                default=0.0,
                max_digits=6,
                null=True,
                verbose_name="menu item mediam price",
            ),
        ),
        migrations.AlterField(
            model_name="resturantmenu",
            name="small_price",
            field=models.DecimalField(
                decimal_places=3,
                default=0.0,
                max_digits=6,
                null=True,
                verbose_name="menu item small price",
            ),
        ),
    ]
