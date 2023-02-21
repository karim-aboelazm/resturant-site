# Generated by Django 4.1.7 on 2023-02-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resturant", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resturantspecials",
            name="full_title_ar",
        ),
        migrations.RemoveField(
            model_name="resturantspecials",
            name="full_title_en",
        ),
        migrations.RemoveField(
            model_name="resturantspecials",
            name="short_title_ar",
        ),
        migrations.RemoveField(
            model_name="resturantspecials",
            name="short_title_en",
        ),
        migrations.AddField(
            model_name="resturantspecials",
            name="category_ar",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Resturant special arabic category",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resturantspecials",
            name="category_en",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Resturant special english category",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resturantspecials",
            name="title_ar",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Resturant special arabic title",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resturantspecials",
            name="title_en",
            field=models.CharField(
                default="",
                max_length=255,
                verbose_name="Resturant special english title",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resturantspecials",
            name="description_ar",
            field=models.TextField(verbose_name="Resturant special arabic description"),
        ),
        migrations.AlterField(
            model_name="resturantspecials",
            name="description_en",
            field=models.TextField(
                verbose_name="Resturant special english description"
            ),
        ),
    ]