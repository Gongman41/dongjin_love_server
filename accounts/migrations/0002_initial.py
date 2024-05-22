# Generated by Django 4.2.8 on 2024-05-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("movies", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="like_genre",
            field=models.ManyToManyField(blank=True, to="movies.genre"),
        ),
        migrations.AddField(
            model_name="user",
            name="like_movie",
            field=models.ManyToManyField(
                blank=True, related_name="liked_users", to="movies.movie"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
