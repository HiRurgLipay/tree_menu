from core.business_logic.templatetags.menu_tags import build_menu
from core.models import MenuItem

from django.shortcuts import render


def menu_view(request, menu_name):
    root_menu_items = MenuItem.objects.filter(parent__isnull=True)
    current_path = request.path_info

    menu_html = build_menu(root_menu_items, current_path)

    context = {
        'menu_html': menu_html,
    }

    return render(request, 'menu_template.html', context)
