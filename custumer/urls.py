from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CustumerListView, CustumerCreateView, CustumerUpdateView, CustumerDeleteView 

app_name = "custumer"
urlpatterns = [
    path("list/", CustumerListView.as_view(), name="custumer_list"),
    path("", CustumerCreateView.as_view(), name="custumer_create"),
    path("<int:id>/", CustumerUpdateView.as_view(), name="custumer_update"),
    path("<int:id>/delete/", CustumerDeleteView.as_view(), name="custumer_delete"),
]