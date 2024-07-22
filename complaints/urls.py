from django.urls import path
from complaints.views import ComplaintListView

app_name = 'complaints'

urlpatterns = [
    path('complaint-list/', ComplaintListView.as_view(), name = 'complaint_list')
]

