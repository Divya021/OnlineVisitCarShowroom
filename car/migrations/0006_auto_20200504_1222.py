# Generated by Django 2.2.2 on 2020-05-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20200503_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='enquery_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='remark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='remark_date',
            field=models.DateTimeField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]