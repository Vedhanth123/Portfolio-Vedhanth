from django.http import HttpResponse

def health_check(request):
    """
    Simple health check endpoint for fly.io monitoring
    """
    return HttpResponse("OK")
