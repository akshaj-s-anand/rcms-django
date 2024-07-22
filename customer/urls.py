from django.urls import path
from customer.views import CustomerDashboardView, CustomerListView, CustomerCreateView, CustomerBulkDeleteView

app_name = 'customers'

urlpatterns = [
    path('dashboard/', CustomerDashboardView.as_view(), name = 'customer_dashboard'),
    path('customer-list', CustomerListView.as_view(), name = 'customer_list'),
    path('add-customer', CustomerCreateView.as_view(), name = 'add_customer'),
    path('customers/bulk-delete/', CustomerBulkDeleteView.as_view(), name='customer_bulk_delete'),
]
