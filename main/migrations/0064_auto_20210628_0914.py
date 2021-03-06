# Generated by Django 3.2.3 on 2021-06-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_alter_heroes_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('deff', 'deff'), ('magatt', 'magatt'), ('physatt', 'physatt')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('shooter', 'shooter'), ('tank', 'tank'), ('magician', 'magician'), ('assassin', 'assassin'), ('support', 'support'), ('fighter', 'fighter')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]
