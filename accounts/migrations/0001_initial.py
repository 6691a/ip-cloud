# Generated by Django 5.0.3 on 2024-03-19 11:39

import django.db.models.deletion
import phonenumber_field.modelfields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Accounts",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_column="created",
                        help_text="Date time on which the object was created.",
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True,
                        db_column="modified",
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified",
                    ),
                ),
                (
                    "email",
                    models.EmailField(db_column="email", max_length=254, unique=True, verbose_name="email address"),
                ),
                ("name", models.CharField(blank=True, db_column="name", max_length=30, verbose_name="name")),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        db_column="gender",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "alias",
                    models.CharField(
                        blank=True, db_column="alias", max_length=12, null=True, unique=True, verbose_name="alias"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, db_column="phone", max_length=128, region=None, verbose_name="phone"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        db_column="active",
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        db_column="staff",
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Account",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.CreateModel(
            name="HistoricalAccounts",
            fields=[
                ("id", models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        db_column="created",
                        editable=False,
                        help_text="Date time on which the object was created.",
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        db_column="modified",
                        editable=False,
                        help_text="Date time on which the object was last modified.",
                        verbose_name="modified",
                    ),
                ),
                (
                    "email",
                    models.EmailField(db_column="email", db_index=True, max_length=254, verbose_name="email address"),
                ),
                ("name", models.CharField(blank=True, db_column="name", max_length=30, verbose_name="name")),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        db_column="gender",
                        max_length=1,
                        verbose_name="gender",
                    ),
                ),
                (
                    "alias",
                    models.CharField(
                        blank=True, db_column="alias", db_index=True, max_length=12, null=True, verbose_name="alias"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, db_column="phone", max_length=128, region=None, verbose_name="phone"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        db_column="active",
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        db_column="staff",
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Account",
                "verbose_name_plural": "historical Accounts",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
