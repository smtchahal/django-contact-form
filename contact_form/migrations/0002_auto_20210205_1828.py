# Generated by Django 3.1.4 on 2021-02-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformsubmission',
            name='subject',
            field=models.CharField(choices=[('Account', 'Account'), ('Payment', 'Payment'), ('General feedback', 'General feedback'), ('Other', 'Other')], max_length=200),
        ),
    ]
