# Generated by Django 3.2.3 on 2021-06-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_heroes_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('Маги', 'Маги'), ('support', 'support'), ('Бойцы', 'Бойцы'), ('assassin', 'assassin'), ('shooter', 'shooter'), ('tank', 'tank')], default='Бойцы', max_length=20, verbose_name='Группа'),
        ),
    ]
