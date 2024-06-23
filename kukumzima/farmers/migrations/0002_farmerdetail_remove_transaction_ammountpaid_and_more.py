# Generated by Django 4.2.13 on 2024-06-23 14:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbfarmerUsername', models.CharField(max_length=100)),
                ('dbfarmerPhonenum', models.CharField(max_length=15)),
                ('dbfarmerPassword', models.CharField(max_length=255)),
                ('dbfarmerEmail', models.EmailField(max_length=100)),
                ('dbfarmerAddress', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'farmer',
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='ammountPaid',
        ),
        migrations.AddField(
            model_name='order',
            name='completeOrderDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='orderDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='amountPaid',
            field=models.PositiveIntegerField(default=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='numberOfHens',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantityOfEggs',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='unitPrice',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='unitPrice',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='farm',
            name='farmer_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmerdetail'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='farmer_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmerdetail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='farmer_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmerdetail'),
        ),
        migrations.DeleteModel(
            name='farmer_detail',
        ),
    ]
