from core.business_logic.templatetags.menu_tags import build_menu
from core.business_logic.services import root_menu_service

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def menu_view(request: HttpRequest, menu_name: str) -> HttpResponse:
    
    root_menu_items = root_menu_service()
    current_path = request.path_info
    menu_html = build_menu(root_menu_items, current_path)
    
    context = {
        'menu_html': menu_html,
    }
    
    return render(request, 'menu_template.html', context)
