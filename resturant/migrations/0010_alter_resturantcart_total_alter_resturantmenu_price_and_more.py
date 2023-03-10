# Generated by Django 4.1.7 on 2023-03-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant", "0009_resturanttablereservasion_confirm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resturantcart",
            name="total",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=6, verbose_name="total"
            ),
        ),
        migrations.AlterField(
            model_name="resturantmenu",
            name="price",
            field=models.DecimalField(
                decimal_places=3, max_digits=6, verbose_name="menu item price"
            ),
        ),
        migrations.AlterField(
            model_name="resturantmenucart",
            name="rate",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=6, verbose_name="rate"
            ),
        ),
        migrations.AlterField(
            model_name="resturantmenucart",
            name="subtotal",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=6, verbose_name="subtotal"
            ),
        ),
        migrations.AlterField(
            model_name="resturantmenuorder",
            name="total",
            field=models.DecimalField(
                decimal_places=3, default=0.0, max_digits=6, verbose_name="total"
            ),
        ),
    ]
