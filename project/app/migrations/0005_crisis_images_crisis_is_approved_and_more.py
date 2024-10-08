# Generated by Django 4.2.16 on 2024-09-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_crisis_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='crisis',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='crisis',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='crisis',
            name='required_help',
            field=models.TextField(default='Not Specified', max_length=300),
        ),
        migrations.AlterField(
            model_name='crisis',
            name='severity',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], max_length=10),
        ),
        migrations.AlterField(
            model_name='crisis',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]
