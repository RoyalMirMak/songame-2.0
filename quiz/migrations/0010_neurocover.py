# Generated by Django 3.2.18 on 2023-07-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20230725_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neurocover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField(default='Вы видите обложку некоторого трека, которая была сгенерирована при помощи нейросетей. Угадайте, что это за трек!', editable=False)),
                ('image_path', models.TextField()),
                ('answer_id', models.IntegerField()),
                ('type', models.TextField(default='emojilate', editable=False)),
            ],
        ),
    ]
