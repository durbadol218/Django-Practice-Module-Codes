# Generated by Django 5.0.6 on 2024-08-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transactionmodel_delete_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdraw'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Send Money'), (6, 'Recieved Money')], null=True),
        ),
    ]
