from bio.models import Human
from django.shortcuts import render_to_response

def show_human_bio(request):
    """
    Simple view for human bio
    """
    human = Human.objects.filter(pk=1)
    return render_to_response("human_bio.html", {'human': human})

