# Generated by Django 4.1.7 on 2023-03-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubation_app', '0018_rename_invites_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
    ]
