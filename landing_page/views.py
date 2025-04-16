from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import HomePageContent
from .forms import HomePageContentContentForm, PricingPlanForm
from django.shortcuts import render, redirect
from .models import PricingPlan


def home(request):
    content = HomePageContent.objects.first()
    plans = PricingPlan.objects.all()

    # Process the features in the view
    for plan in plans:
        plan.features_list = plan.features.split(',')  # Create a list of features

    return render(request, 'home.html', {'content': content, 'plans':plans})

def dashboard(request):
    return render(request, 'dashboard.html')


def manage_homepage(request):
    content, created = HomePageContent.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = HomePageContentContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes have been saved successfully!')

            return redirect('manage_homepage')
    else:
        form = HomePageContentContentForm(instance=content)
    return render(request, 'manage_homepage.html', {'form': form})


def pricing_plans(request):
    plans = PricingPlan.objects.all()
    
    if request.method == "POST":
        form = PricingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pricing_plans')
    else:
        form = PricingPlanForm()

    return render(request, 'pricing_plans.html', {'form': form, 'plans': plans})


def edit_plan(request, pk):
    plan = get_object_or_404(PricingPlan, pk=pk)
    form = PricingPlanForm(request.POST or None, instance=plan)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Plan updated successfully!")
        return redirect('pricing_plans')
    return render(request, 'edit_plan.html', {'form': form})


def delete_plan(request, pk):
    plan = get_object_or_404(PricingPlan, pk=pk)
    plan.delete()
    messages.success(request, "Plan deleted successfully!")
    return redirect('pricing_plans')