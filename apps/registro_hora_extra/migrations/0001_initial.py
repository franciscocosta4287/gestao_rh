# Generated by Django 4.1.7 on 2023-03-15 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("funcionarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegistroHE",
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
                ("motivo", models.CharField(max_length=100)),
                (
                    "funcionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="funcionarios.funcionario",
                    ),
                ),
            ],
        ),
    ]
