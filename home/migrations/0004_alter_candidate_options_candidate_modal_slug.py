# Generated by Django 4.2.6 on 2023-10-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_candidate_modal_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name_plural': 'Candidate'},
        ),
        migrations.AddField(
            model_name='candidate',
            name='modal_slug',
            field=models.SlugField(default=5478390745839203759340858934028, max_length=300),
            preserve_default=False,
        ),
    ]
