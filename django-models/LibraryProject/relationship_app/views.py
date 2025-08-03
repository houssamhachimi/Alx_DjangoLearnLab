from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
