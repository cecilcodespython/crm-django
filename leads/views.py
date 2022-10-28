from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm
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
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent,
            )
            return redirect("/leads")

    
    return render(request,'leads/lead_create.html',{
        'form':form
    })

   


    