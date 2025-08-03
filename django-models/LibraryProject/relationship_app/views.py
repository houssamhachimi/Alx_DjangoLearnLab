from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_role(role):
    def predicate(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(predicate)

@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
