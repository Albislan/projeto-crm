from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Custumer
from .forms import CustumerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

class CustumerListView(ListView):
    template_name = "custumer/custumer_list.html"
    paginate_by = 10
    model = Custumer
    
    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            object_list = self.model.objects.filter(Q(first_name__icontains=name)
                                                    | Q(last_name__icontains=name))
        else:
            object_list = self.model.objects.all()
        return object_list    


class CustumerCreateView(CreateView):
    template_name = "custumer/custumer.html"
    form_class = CustumerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("custumer:custumer_list")    


class CustumerUpdateView(UpdateView):
    template_name = "custumer/custumer.html"
    form_class = CustumerForm

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Custumer, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("custumer:custumer_list") 


class CustumerDeleteView(DeleteView):
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Custumer, id=id)

    def get_success_url(self):
        return reverse("custumer:custumer_list") 


