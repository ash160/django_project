
from django.urls import path
from home.models import Personal,Address,Salary,Otherincome,House_property,Deduction,More_deduction,Tds,DocumentUpload
from django.shortcuts import render, redirect
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse  
from home.functions import handle_uploaded_file  
from home.forms import StudentForm  


# Create your views here.

def index(request):
    return render(request,'personal.html')
def addresss(request):
    return render(request,'Address.html')
def salaryy(request):
    return render(request,'Salary.html')
def otherincome(request):
    return render(request,'Otherincome.html')
def house(request):
    return render(request,'HouseProperty.html')
def capital(request):
    return render(request,'CapitalGain.html')
def deduction(request):
    return render(request,'Deductions.html')
def morededuction(request):
    return render(request,'MoreDeductions.html')
def otherdeduction(request):
    return render(request,'EvenMoreDeductions.html')
def investmentdetails(request):
    return render(request,'TdsSummary.html')
def tds(request):
    return render(request,'AddTds.html')
def upload(request):
    return render(request,'Upload.html')

def selftax(request):
    return render(request,'TaxesPaidSummary.html')
def TaxesPaidSummary6e35(request):
    return render(request,'TaxesPaidSummary_next.html') 

def personal(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        mid=request.POST.get('mid')
        last_name=request.POST.get('last_name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pan_number=request.POST.get('pan_number')
        father_name=request.POST.get('father_name')
        
        marital_status=request.POST.get('marital_status')
        personal=Personal(first_name=first_name,mid=mid,last_name=last_name,gender=gender,dob=dob,pan_number=pan_number,father_name=father_name,marital_status=marital_status)
        personal.save()
    return render(request,'Address.html')

def address(request):
    if request.method=='POST':
        flat_num=request.POST.get('flat_num')
        premise_name=request.POST.get('premise_name')
        road_name=request.POST.get('road_name')
        pincode=request.POST.get('pincode')
        area =request.POST.get('area')
        town_name=request.POST.get('town_name')
        state_name=request.POST.get('state_name')
        country_name=request.POST.get('country_name')
        contact_number=request.POST.get('contact_number')
        email=request.POST.get('email')
        email2=request.POST.get('email2')
        address=Address(flat_num=flat_num,premise_name=premise_name,road_name=road_name,pincode=pincode,area=area,town_name=town_name,state_name=state_name,country_name=country_name,contact_number=contact_number,email=email,email2=email2)
        address.save()
    return render(request,'Salary.html')

def salary(request):
    if request.method=='POST':
        employer_name=request.POST.get('employer_name')
        employer_type=request.POST.get('employer_type')
        salary=request.POST.get('salary')
        perquisites=request.POST.get('perquisites')
        profit=request.POST.get('profit')
        allowances=request.POST.get('allowances')
        balance=request.POST.get('balance')
        #deduction=request.POST.get('deduction')
        std_deduciton=request.POST.get('std_deduciton')
        professional_tax=request.POST.get('professional_tax')
        income_chargeable=request.POST.get('income_chargeable')
        tds=request.POST.get('tds')
        tan=request.POST.get('tan')
        sal=Salary(employer_name=employer_name,employer_type=employer_type,salary=salary,perquisites=perquisites,
        profit=profit,allowances=allowances,balance=balance,std_deduciton=std_deduciton,
        professional_tax=professional_tax,income_chargeable=income_chargeable,tds=tds,tan=tan)
        sal.save()
    return render(request,'Otherincome.html')

def Otherincomee(request):
    if request.method=='POST':
        savingsbank=request.POST.get('savingsbank')
        deposit=request.POST.get('deposit')
        interest_income=request.POST.get('interest_income')
        any_other_interest_income=request.POST.get('any_other_interest_income')
        any_other_income=request.POST.get('any_other_income')
        dividend_income=request.POST.get('dividend_income')
        dividend_income_from_Mutual_fund=request.POST.get('dividend_income_from_Mutual_fund')
        ppf=request.POST.get('ppf')
        any_other=request.POST.get('any_other')
        gross_agriculture=request.POST.get('gross_agriculture')
        expenditure_on_agriculture=request.POST.get('expenditure_on_agriculture')
        unabsorbed_agriculture_loss=request.POST.get('unabsorbed_agriculture_loss')
        agriculture_land_details1=request.POST.get('agriculture_land_details1')
        agriculture_land_details2=request.POST.get('agriculture_land_details2')
        agriculture_land_details3=request.POST.get('agriculture_land_details3')
        agriculture_land_details4=request.POST.get('agriculture_land_details4')
        agriculture_land_details5=request.POST.get('agriculture_land_details5')
        other=Otherincome(savingsbank=savingsbank,deposit=deposit,interest_income=interest_income,any_other_interest_income=any_other_interest_income,any_other_income=any_other_income,dividend_income=dividend_income,dividend_income_from_Mutual_fund=dividend_income_from_Mutual_fund,ppf=ppf,any_other=any_other,gross_agriculture=gross_agriculture,expenditure_on_agriculture=expenditure_on_agriculture,unabsorbed_agriculture_loss=unabsorbed_agriculture_loss,agriculture_land_details1=agriculture_land_details1,agriculture_land_details2=agriculture_land_details2,agriculture_land_details3=agriculture_land_details3,agriculture_land_details4=agriculture_land_details4,agriculture_land_details5=agriculture_land_details5)
        other.save()
    return render(request,'HouseProperty.html')

def house_property(request):
    if request.method=="POST":

        Type_of_House_Property=request.POST.get('Type_of_House_Property')
        Interest_paid_on_loan_for_this_house_property=request.POST.get('Interest_paid_on_loan_for_this_house_property')
        year=request.POST.get('year')
        Total_interest_amount_paid_during_the_pre_construction_period=request.POST.get('Total_interest_amount_paid_during_the_pre_construction_period')
        #Same_as_the_address_in_Personal_Info=request.POST.get('Same_as_the_address_in_Personal_Info')
        flat_num=request.POST.get('flat_num')
        premise_name=request.POST.get('premise_name')
        road_name=request.POST.get('road_name')
        pincode=request.POST.get('pincode')
        area=request.POST.get('area')
        town_name=request.POST.get('town_name')
        state_name=request.POST.get('state_name')
        country_name=request.POST.get('country_name')   
        Name_of_Co_Owner1=request.POST.get('Name_of_Co_Owner1')
        pan_of_Co_Owner1=request.POST.get('pan_of_Co_Owner1')
        percentage_of_Co_Owner1=request.POST.get('percentage_of_Co_Owner1')
        
        #Name_of_Co_Owner2=request.POST.get('Name_of_Co_Owner2')
        #pan_of_Co_Owner2=request.POST.get('pan_of_Co_Owner2')
        #percentage_of_Co_Owner2=request.POST.get('percentage_of_Co_Owner3')
        
        ho=House_property(Type_of_House_Property=Type_of_House_Property,Interest_paid_on_loan_for_this_house_property=Interest_paid_on_loan_for_this_house_property,year=year,Total_interest_amount_paid_during_the_pre_construction_period=Total_interest_amount_paid_during_the_pre_construction_period,flat_num=flat_num,premise_name=premise_name,road_name=road_name,pincode=pincode,area=area,town_name=town_name,state_name=state_name,country_name=country_name,Name_of_Co_Owner1=Name_of_Co_Owner1,pan_of_Co_Owner1=pan_of_Co_Owner1,percentage_of_Co_Owner1=percentage_of_Co_Owner1)#Same_as_the_address_in_Personal_Info=Same_as_the_address_in_Personal_Info,,Name_of_Co_Owner2=Name_of_Co_Owner2,pan_of_Co_Owner2=pan_of_Co_Owner2,percentage_of_Co_Owner2=percentage_of_Co_Owner2      
        ho.save()

    return render(request,'AddTds.html')

#deduction/sectionn80 form
def section80(request):
    if request.method=="POST":

        Investment_for_Section=request.POST.get('Investment_for_Section')
        Interest_earned_on_Savings_Bank_Account=request.POST.get('Interest_earned_on_Savings_Bank_Account')
        sec=Deduction(Investment_for_Section=Investment_for_Section,Interest_earned_on_Savings_Bank_Account=Interest_earned_on_Savings_Bank_Account)
        sec.save()
    return render(request,'MoreDeductions.html')

#morededuction view and model is More_deduction
def more_deduction(request):
    if request.method=="POST":
            
        For_Parents=request.POST.get('For_Parents')
        Medical_Insurance_Premium1=request.POST.get('Medical_Insurance_Premium1')
        Medical_Insurance_Premium2=request.POST.get('Medical_Insurance_Premium2')
        Preventive_Health_Check_Up_Fees1=request.POST.get('Preventive_Health_Check_Up_Fees1')
        Preventive_Health_Check_Up_Fees2=request.POST.get('Preventive_Health_Check_Up_Fees2')
        Education_Loan_on_higher_studies=request.POST.get('Education_Loan_on_higher_studies')
        Contribution_to_Pension_Plan=request.POST.get('Contribution_to_Pension_Plan')
        Contribution_towards_Section_80CCD=request.POST.get('Contribution_towards_Section_80CCD')
        Employers_contribution_towards_NPS=request.POST.get('Employers_contribution_towards_NPS')
        Rent_Paid_Per_Month=request.POST.get('Rent_Paid_Per_Month')
        Number_of_Months_Rent_Paid=request.POST.get('Number_of_Months_Rent_Paid')
        Medical_Treatment_Costs=request.POST.get('Medical_Treatment_Costs')
        Age_of_person=request.POST.get('Age_of_person')
        Deductions_under_Section=request.POST.get('Deductions_under_Section')
        Deductions_under_Section_80EEA=request.POST.get('Deductions_under_Section_80EEA')
        Deductions_under_Section_80EEB=request.POST.get('Deductions_under_Section_80EEB')
        Section_80QQB=request.POST.get('Section_80QQB')
        Section_80RRB=request.POST.get('Section_80RRB')
        Section_80GGC=request.POST.get('Section_80GGC')
        Section_80JJA=request.POST.get('Section_80JJA')
        Section_80GGA=request.POST.get('Section_80GGA')
        more=More_deduction( For_Parents= For_Parents,Medical_Insurance_Premium1=Medical_Insurance_Premium1,Medical_Insurance_Premium2=Medical_Insurance_Premium2,Preventive_Health_Check_Up_Fees1=Preventive_Health_Check_Up_Fees1,Preventive_Health_Check_Up_Fees2=Preventive_Health_Check_Up_Fees2,Education_Loan_on_higher_studies=Education_Loan_on_higher_studies,Contribution_to_Pension_Plan=Contribution_to_Pension_Plan,Contribution_towards_Section_80CCD=Contribution_towards_Section_80CCD,Employers_contribution_towards_NPS=Employers_contribution_towards_NPS,Rent_Paid_Per_Month=Rent_Paid_Per_Month,Number_of_Months_Rent_Paid=Number_of_Months_Rent_Paid,Medical_Treatment_Costs=Medical_Treatment_Costs,Age_of_person=Age_of_person,Deductions_under_Section=Deductions_under_Section,Deductions_under_Section_80EEA=Deductions_under_Section_80EEA,Deductions_under_Section_80EEB=Deductions_under_Section_80EEB,Section_80QQB=Section_80QQB,Section_80RRB=Section_80RRB,Section_80GGC=Section_80GGC,Section_80JJA=Section_80JJA,Section_80GGA=Section_80GGA)
        more.save()
    return render(request,'AddTds.html')

#tax paid/tds view model Tds
def tds_view(request):
    if request.method=='POST':

        TAN_of_Deductor=request.POST.get('TAN_of_Deductor')
        Name_of_Deductor=request.POST.get('Name_of_Deductor')
        Total_Tax_Deducted=request.POST.get('Total_Tax_Deducted')
        Tax_Deducted_claimed_for_this_year=request.POST.get('Tax_Deducted_claimed_for_this_year')
        Income_against_which_TDS_was_deducted=request.POST.get('Income_against_which_TDS_was_deducted')
        
        Type_of_Income=request.POST.get('Type_of_Income')
        Financial_Year_in_which_TDS_was_deducted=request.POST.get('Financial_Year_in_which_TDS_was_deducted')

        td=Tds(TAN_of_Deductor=TAN_of_Deductor,Name_of_Deductor=Name_of_Deductor,Total_Tax_Deducted=Total_Tax_Deducted,Tax_Deducted_claimed_for_this_year=Tax_Deducted_claimed_for_this_year,Income_against_which_TDS_was_deducted=Income_against_which_TDS_was_deducted,Type_of_Income=Type_of_Income,Financial_Year_in_which_TDS_was_deducted=Financial_Year_in_which_TDS_was_deducted)
        td.save()
    return render(request,'thank.html')




def uploader(request):
    if request.method=="POST" and  request.FILES['file']:
        
        file = request.FILES['file']

        doc=DocumentUpload(upload_file=file)
        doc.save()
        return redirect('salary')
    return render(request, 'fileupload.html')