# Generated by Django 3.0.5 on 2024-05-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Tim mạch', 'Tim mạch'), ('Da liễu', 'Da liễu'), ('Chuyên gia Cấp cứu', 'Chuyên gia Cấp cứu'), ('Dị ứng/Miễn dịch', 'Dị ứng/Miễn dịch'), ('Gây mê', 'Gây mê'), ('Phẫu thuật Đại tràng & Trực tràng', 'Phẫu thuật Đại tràng & Trực tràng')], default='Tim mạch', max_length=50),
        ),
    ]
