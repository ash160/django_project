from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('per',views.personal,name='index'),
    path('addresss',views.addresss,name='adress'),
    path('add',views.address,name='add'),
    path('salary',views.salaryy,name='salary'),
    path('sal',views.salary,name='sal'),

    path('otherincome',views.otherincome,name='sal'),
    path('house',views.house,name='house'),
    path('capital',views.capital,name='capital'),
    path('deduction',views.deduction,name='deduction'),
    path('morededuction',views.morededuction,name='morededuction'),
    path('otherdeduction',views.otherdeduction,name='otherdeduction'),
    path('investmentdetails',views.investmentdetails,name='investmentdetails'),
    path('tds',views.tds,name='tds'),
    path('selftax',views.selftax,name='selftax'),
    path('TaxesPaidSummary',views.TaxesPaidSummary6e35,name='TaxesPaidSummary'),
    
    path('uploader',views.uploader,name='Uploader'),#file upload part

    path('otherincome_view',views.Otherincomee,name='otherincome_view'),# it is for otherincome form
    path('house_property_model',views.house_property,name='house_property_model'),#it is for house property form
    path('deduction_section', views.section80,name='deduction_section'),# form in deduction/section80 form
    path('more_deduction_form',views.more_deduction,name='more_deduction_form'),# form for more deduction page
    path('tds_view_form',views.tds_view,name='tds_view_form'),#form of addtds.html

    
  
    
]