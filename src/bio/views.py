from bio.models import Contacts
from django.shortcuts import render_to_response


def show_human_bio(request):
    """
    Simple view for human bio
    """
    human_bio = Contacts.objects.filter(human__id=1).get()
    return render_to_response("human_bio.html", {'humans': [human_bio]})
