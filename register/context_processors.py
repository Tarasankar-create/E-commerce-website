from django.conf import settings

def user_info(request):
    return {
        'name': request.session.get('name', None),
        'pin': request.session.get('pin', None),
    }
# This will send the data to all pages