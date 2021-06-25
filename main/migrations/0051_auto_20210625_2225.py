# Generated by Django 3.2.3 on 2021-06-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20210617_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('magatt', 'magatt'), ('deff', 'deff'), ('physatt', 'physatt')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('assassin', 'assassin'), ('shooter', 'shooter'), ('fighter', 'fighter'), ('support', 'support'), ('tank', 'tank'), ('magician', 'magician')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]
