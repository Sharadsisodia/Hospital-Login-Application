# Generated by Django 5.0.6 on 2024-07-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_Firstname', models.CharField(max_length=50)),
                ('d_Lastname', models.CharField(max_length=50)),
                ('d_Picture', models.ImageField(upload_to='images/')),
                ('d_Username', models.CharField(max_length=20)),
                ('d_EmailId', models.CharField(max_length=50)),
                ('d_Password', models.CharField(max_length=20)),
                ('d_AddressLi', models.TextField()),
                ('d_City', models.CharField(max_length=25)),
                ('d_State', models.CharField(max_length=25)),
                ('d_Pincode', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_Firstname', models.CharField(max_length=50)),
                ('p_Lastname', models.CharField(max_length=50)),
                ('p_Picture', models.ImageField(upload_to='images/')),
                ('p_Username', models.CharField(max_length=20)),
                ('p_EmailId', models.CharField(max_length=50)),
                ('p_Password', models.CharField(max_length=20)),
                ('p_AddressLi', models.TextField()),
                ('p_City', models.CharField(max_length=25)),
                ('p_State', models.CharField(max_length=25)),
                ('p_Pincode', models.IntegerField(max_length=9)),
            ],
        ),
    ]
