# Generated by Django 4.2.6 on 2023-11-06 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0015_alter_paymenthistory_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_profiles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='number_of_votes',
            field=models.CharField(choices=[('8', '8'), ('3', '3'), ('5', '5')], default='Free', max_length=30),
        ),
        migrations.AlterField(
            model_name='usersubscriptions',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]