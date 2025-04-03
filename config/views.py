from django.http.response import HttpResponse, JsonResponse

#Function-Based View
def hello_world(request):
    return HttpResponse("<h1>Hello World<h1>")

def hello_world_jsoin(request):
    return JsonResponse({"message": "Hello, World!"})