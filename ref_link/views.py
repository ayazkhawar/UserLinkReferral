from django.shortcuts import render
from .models import Profile

def my_recommendations_view(request):
    profile = Profile.objects.get(user=request.user)
    my_recs = profile.get_recommend_profiles()
    
    context = {'my_recs': my_recs}
    return render(request, 'ref_link/main.html', context)