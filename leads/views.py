from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm
from django.shortcuts import redirect

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    return render(request,"leads\homepage.html",{
        "leads":leads
    })


def lead_details(request,pk):
    lead = Lead.objects.get(id=pk)
    return render(request,'leads/lead_detail.html',{
        'lead':lead
    })


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    
    return render(request,'leads/lead_create.html',{
        'form':form
    })


def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
   
    context = {
            'form':form,
            'lead':lead
        }
          
            

    return render(request,'leads/lead_update.html',context)


def lead_delete(requests,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


   


    