# Generated by Django 3.1.4 on 2020-12-02 17:31

from django.db import migrations, models

"""
create tables:  commons_ageranges, 
                commons_categories,
                commons_incomeranges
"""


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range_from', models.IntegerField()),
                ('range_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeRanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range_from', models.IntegerField()),
                ('range_to', models.IntegerField()),
            ],
        ),
    ]
