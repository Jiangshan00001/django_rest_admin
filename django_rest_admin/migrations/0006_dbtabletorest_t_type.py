# Generated by Django 3.2 on 2021-11-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_admin', '0005_alter_dbtabletorest_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbtabletorest',
            name='t_type',
            field=models.TextField(blank=True, help_text='table/view', null=True),
        ),
    ]