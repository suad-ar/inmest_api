from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

def say_hello(request):
    return HttpResponse("<h1>Hello World! Welcome to main</h1>")

user = {"name":"Suad", "email": "suad.abdelrahman@meltwater.org", "phoneNumber": "023456789"}

def user_profile(request):
    return JsonResponse(user)

data = [
    {"id":1, "title":"Python Django", "description": "django tutorial", "status":"Open", "submitted_by": "Suad"}, 
    {"id":2, "title":"Flutter Dart", "description": "flutter tutorial", "status":"Pending", "submitted_by": "Grace"}

]

def filter_queries(request, query_id):
    for query in data:
        if query['id'] == query_id:
            return JsonResponse(query)
    return HttpResponse("Query not found")

class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama declined Val shots"},
            {"id":2, "title": "Samson declined Val shots"}
        ]
    def get(self, request):
        return JsonResponse({"result": self.queries})
    def post(self,request):
        return JsonResponse({"status:" "ok"})