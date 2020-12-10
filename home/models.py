from django.db import models

# personal info
class Personal(models.Model):

    first_name=models.CharField(max_length=50,blank=True)
    mid=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=50,blank=True)
    dob=models.DateField()
    pan_number=models.CharField(max_length=50,blank=True)
    father_name=models.CharField(max_length=50,blank=True)
    
    marital_status=models.CharField(max_length=50,blank=True)
    
class Address(models.Model):
    flat_num=models.CharField(max_length=50,blank=True)
    premise_name=models.CharField(max_length=50,blank=True)
    road_name=models.CharField(max_length=50,blank=True)
    pincode=models.CharField(max_length=50,blank=True)
    area =models.CharField(max_length=50,blank=True)
    town_name=models.CharField(max_length=50,blank=True)
    state_name=models.CharField(max_length=50,blank=True)
    country_name=models.CharField(max_length=50,blank=True)
    contact_number=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=50,blank=True)
    email2=models.EmailField(max_length=50,blank=True)
#income/salary
class Salary(models.Model):
    employer_name=models.CharField(max_length=50,blank=True)
    employer_type=models.CharField(max_length=50,blank=True)
    salary=models.CharField(max_length=50,blank=True)
    perquisites=models.CharField(max_length=50,blank=True)
    profit=models.CharField(max_length=50,blank=True)
    allowances=models.CharField(max_length=50,blank=True)
    balance=models.CharField(max_length=50,blank=True)
    deduction=models.CharField(max_length=50,blank=True)
    std_deduciton=models.CharField(max_length=50,blank=True)
    professional_tax=models.CharField(max_length=50,blank=True)
    income_chargeable=models.CharField(max_length=50,blank=True)
    tds=models.CharField(max_length=50,blank=True)
    tan=models.CharField(max_length=50,blank=True)

# /income/other income
class Otherincome(models.Model):
    savingsbank=models.CharField(max_length=50,blank=True)
    deposit=models.CharField(max_length=50,blank=True)
    interest_income=models.CharField(max_length=50,blank=True)
    any_other_interest_income=models.CharField(max_length=50,blank=True)
    any_other_income=models.CharField(max_length=50,blank=True)
    dividend_income =models.CharField(max_length=50,blank=True)
    dividend_income_from_Mutual_fund=models.CharField(max_length=50,blank=True)
    ppf=models.CharField(max_length=50,blank=True)
    any_other=models.CharField(max_length=50,blank=True)
    gross_agriculture=models.CharField(max_length=50,blank=True)
    expenditure_on_agriculture=models.CharField(max_length=50,blank=True)
    unabsorbed_agriculture_loss=models.CharField(max_length=50,blank=True)
    
    agriculture_land_details1=models.CharField(max_length=50,blank=True)
    agriculture_land_details2=models.CharField(max_length=50,blank=True)
    agriculture_land_details3=models.CharField(max_length=50,blank=True)
    agriculture_land_details4=models.CharField(max_length=50,blank=True)
    agriculture_land_details5=models.CharField(max_length=50,blank=True)

#income/house property
class House_property(models.Model):
    Type_of_House_Property=models.CharField(max_length=50,blank=True)
    Interest_paid_on_loan_for_this_house_property=models.CharField(max_length=50,blank=True)
    year=models.CharField(max_length=50,blank=True)
    Total_interest_amount_paid_during_the_pre_construction_period=models.CharField(max_length=50,blank=True)
    Same_as_the_address_in_Personal_Info=models.CharField(max_length=50,blank=True)
    flat_num=models.CharField(max_length=50,blank=True)
    premise_name=models.CharField(max_length=50,blank=True)
    road_name=models.CharField(max_length=50,blank=True)
    pincode=models.CharField(max_length=50,blank=True)
    area =models.CharField(max_length=50,blank=True)
    town_name=models.CharField(max_length=50,blank=True)
    state_name=models.CharField(max_length=50,blank=True)
    country_name=models.CharField(max_length=50,blank=True)   
    Name_of_Co_Owner1=models.CharField(max_length=50,blank=True)
    pan_of_Co_Owner1=models.CharField(max_length=50,blank=True)
    percentage_of_Co_Owner1=models.CharField(max_length=50,blank=True)
    Name_of_Co_Owner2=models.CharField(max_length=50,blank=True)
    pan_of_Co_Owner2=models.CharField(max_length=50,blank=True)
    percentage_of_Co_Owner2=models.CharField(max_length=50,blank=True)

#deduction.html / first page form
class Deduction(models.Model):
    Investment_for_Section=models.CharField(max_length=50,blank=True)
    Interest_earned_on_Savings_Bank_Account=models.CharField(max_length=50,blank=True)

#deduction/more deduction
class More_deduction(models.Model):
    For_Parents=models.CharField(max_length=50,blank=True)
    Medical_Insurance_Premium1=models.CharField(max_length=50,blank=True)
    Medical_Insurance_Premium2=models.CharField(max_length=50,blank=True)
    Preventive_Health_Check_Up_Fees1=models.CharField(max_length=50,blank=True)
    Preventive_Health_Check_Up_Fees2=models.CharField(max_length=50,blank=True)
    Education_Loan_on_higher_studies=models.CharField(max_length=50,blank=True)
    Contribution_to_Pension_Plan=models.CharField(max_length=50,blank=True)
    Contribution_towards_Section_80CCD=models.CharField(max_length=50,blank=True)
    Employers_contribution_towards_NPS=models.CharField(max_length=50,blank=True)
    Rent_Paid_Per_Month=models.CharField(max_length=50,blank=True)
    
    Number_of_Months_Rent_Paid=models.CharField(max_length=50,blank=True)
    Medical_Treatment_Costs=models.CharField(max_length=50,blank=True)
    Age_of_person=models.CharField(max_length=50,blank=True)
    Deductions_under_Section=models.CharField(max_length=50,blank=True)
    Deductions_under_Section_80EEA=models.CharField(max_length=50,blank=True)
    Deductions_under_Section_80EEB=models.CharField(max_length=50,blank=True)
    Section_80QQB=models.CharField(max_length=50,blank=True)
    Section_80RRB=models.CharField(max_length=50,blank=True)
    Section_80GGC=models.CharField(max_length=50,blank=True)
    Section_80JJA=models.CharField(max_length=50,blank=True)
    Section_80GGA=models.CharField(max_length=50,blank=True)

class Tds(models.Model):
    TAN_of_Deductor=models.CharField(max_length=50,blank=True)
    Name_of_Deductor=models.CharField(max_length=50,blank=True)
    Total_Tax_Deducted=models.CharField(max_length=50,blank=True)
    Tax_Deducted_claimed_for_this_year=models.CharField(max_length=50,blank=True)
    Income_against_which_TDS_was_deducted=models.CharField(max_length=50,blank=True)
    Type_of_Income=models.CharField(max_length=50,blank=True)
    Financial_Year_in_which_TDS_was_deducted=models.CharField(max_length=50,blank=True)



class DocumentUpload(models.Model):
    
    upload_file = models.FileField(upload_to='doc/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add =True)












