# Generated by Django 4.2.6 on 2023-12-20 07:41

from django.db import migrations, models
import utilmeta.core.orm.backends.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=utilmeta.core.orm.backends.django.models.ACASCADE,
                        related_name="user_favorites",
                        to="article.article",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=40, unique=True)),
                (
                    "password",
                    utilmeta.core.orm.backends.django.models.PasswordField(
                        max_length=100, min_length=1, regex=None, salt_length=32
                    ),
                ),
                ("email", models.EmailField(max_length=60, unique=True)),
                ("token", models.TextField(default="")),
                ("bio", models.TextField(default="")),
                ("image", models.URLField(default="")),
                (
                    "favorites",
                    models.ManyToManyField(
                        related_name="favorited_bys",
                        through="user.Favorite",
                        to="article.article",
                    ),
                ),
                (
                    "followers",
                    models.ManyToManyField(
                        related_name="followed_bys",
                        through="user.Follow",
                        to="user.user",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="follow",
            name="follower",
            field=models.ForeignKey(
                on_delete=utilmeta.core.orm.backends.django.models.ACASCADE,
                related_name="user_followings",
                to="user.user",
            ),
        ),
        migrations.AddField(
            model_name="follow",
            name="following",
            field=models.ForeignKey(
                on_delete=utilmeta.core.orm.backends.django.models.ACASCADE,
                related_name="user_followers",
                to="user.user",
            ),
        ),
        migrations.AddField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                on_delete=utilmeta.core.orm.backends.django.models.ACASCADE,
                related_name="article_favorites",
                to="user.user",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="follow",
            unique_together={("following", "follower")},
        ),
        migrations.AlterUniqueTogether(
            name="favorite",
            unique_together={("user", "article")},
        ),
    ]
