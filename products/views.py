import json

from django.http  import JsonResponse
from django.views import View

from products.models import Menu, Category, Drink

class ProductsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.create(name = data["menu"])
        category = Category.objects.create(
            name = data["category"],
            menu = menu
        )
        Drink.objects.create(
            name     = data["drink"], 
            category = category
        )
        return JsonResponse({"messasge" : "created"}, status = 201)