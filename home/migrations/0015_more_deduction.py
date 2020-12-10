# Generated by Django 3.1.3 on 2020-12-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_deduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='More_deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('For_Parents', models.CharField(blank=True, max_length=50)),
                ('Medical_Insurance_Premium1', models.CharField(blank=True, max_length=50)),
                ('Medical_Insurance_Premium2', models.CharField(blank=True, max_length=50)),
                ('Preventive_Health_Check_Up_Fees1', models.CharField(blank=True, max_length=50)),
                ('Preventive_Health_Check_Up_Fees2', models.CharField(blank=True, max_length=50)),
                ('Education_Loan_on_higher_studies', models.CharField(blank=True, max_length=50)),
                ('Contribution_to_Pension_Plan', models.CharField(blank=True, max_length=50)),
                ('Contribution_towards_Section_80CCD', models.CharField(blank=True, max_length=50)),
                ('Employers_contribution_towards_NPS', models.CharField(blank=True, max_length=50)),
                ('Rent_Paid_Per_Month', models.CharField(blank=True, max_length=50)),
                ('Number_of_Months_Rent_Paid', models.CharField(blank=True, max_length=50)),
                ('Medical_Treatment_Costs', models.CharField(blank=True, max_length=50)),
                ('Age_of_person', models.CharField(blank=True, max_length=50)),
                ('Deductions_under_Section', models.CharField(blank=True, max_length=50)),
                ('Deductions_under_Section_80EEA', models.CharField(blank=True, max_length=50)),
                ('Deductions_under_Section_80EEB', models.CharField(blank=True, max_length=50)),
                ('Section_80QQB', models.CharField(blank=True, max_length=50)),
                ('Section_80RRB', models.CharField(blank=True, max_length=50)),
                ('Section_80GGC', models.CharField(blank=True, max_length=50)),
                ('Section_80JJA', models.CharField(blank=True, max_length=50)),
                ('Section_80GGA', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]