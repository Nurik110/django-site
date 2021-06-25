# Generated by Django 3.2.3 on 2021-06-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_alter_heroes_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('deff', 'deff'), ('physatt', 'physatt'), ('magatt', 'magatt')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('shooter', 'shooter'), ('tank', 'tank'), ('magician', 'magician'), ('fighter', 'fighter'), ('assassin', 'assassin'), ('support', 'support')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]