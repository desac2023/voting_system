# Generated by Django 4.2.6 on 2023-11-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_subscription_number_of_votes_voting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='modal_image',
        ),
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='templates/uploads/'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='number_of_votes',
            field=models.CharField(choices=[('3', '3'), ('5', '5'), ('8', '8')], default='Free', max_length=30),
        ),
    ]