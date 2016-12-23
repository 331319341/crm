from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from team.models import Team, Employee
from customer.models import Project, Customer, Order, Contract

content_type_team = ContentType.objects.get_for_model(Team)
content_type_employee = ContentType.objects.get_for_model(Employee)
content_type_project = ContentType.objects.get_for_model(Project)
content_type_customer = ContentType.objects.get_for_model(Customer)
content_type_order = ContentType.objects.get_for_model(Order)
content_type_contract = ContentType.objects.get_for_model(Contract)
'''
add_team_permission
change_team_permission
delete_team_permission 

add_employee_permission 
change_employee_permission 
delete_employee_permission

add_order_permission 
change_order_permission 
delete_order_permission 

add_contract_permission 
change_contract_permission
delete_contract_permission 

add_customer_permission 
change_customer_permission 
delete_customer_permission

add_project_permission 
change_project_permission
delete_project_permission 

'''
add_team_permission = Permission.objects.get(codename='add_team', content_type=content_type_team)
change_team_permission = Permission.objects.get(codename='change_team', content_type=content_type_team)
delete_team_permission = Permission.objects.get(codename='delete_team', content_type=content_type_team)

add_employee_permission = Permission.objects.get(codename='add_employee', content_type=content_type_employee)
change_employee_permission = Permission.objects.get(codename='change_employee', content_type=content_type_employee)
delete_employee_permission = Permission.objects.get(codename='delete_employee', content_type=content_type_employee)

add_order_permission = Permission.objects.get(codename='add_order', content_type=content_type_order)
change_order_permission = Permission.objects.get(codename='change_order', content_type=content_type_order)
delete_order_permission = Permission.objects.get(codename='delete_order', content_type=content_type_order)

add_contract_permission = Permission.objects.get(codename='add_contract', content_type=content_type_contract)
change_contract_permission = Permission.objects.get(codename='change_contract', content_type=content_type_contract)
delete_contract_permission = Permission.objects.get(codename='delete_contract', content_type=content_type_contract)

add_customer_permission = Permission.objects.get(codename='add_customer', content_type=content_type_customer)
change_customer_permission = Permission.objects.get(codename='change_customer', content_type=content_type_customer)
delete_customer_permission = Permission.objects.get(codename='delete_customer', content_type=content_type_customer)

add_project_permission = Permission.objects.get(codename='add_project', content_type=content_type_project)
change_project_permission = Permission.objects.get(codename='change_project', content_type=content_type_project)
delete_project_permission = Permission.objects.get(codename='delete_project', content_type=content_type_project)
