from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tracking, BestDefact

# Create your views here.
@login_required
def analysis(request):
	products = ['SecuMS', 'OmniGuard Unix', 'OmniGuard Windows', 'FOSSGuard', 'Athena']

	trackings = [Tracking.objects.filter(product__icontains=products[i], is_deleted=True) for i, x in enumerate(products)]

	bestdefacts = BestDefact.objects.all()
	
	return render(request, 'analysis/analysis.html', {'products':products, 'trackings':trackings, 'bestdefacts':bestdefacts})