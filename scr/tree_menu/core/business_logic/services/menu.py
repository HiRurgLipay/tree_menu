from core.models import MenuItem


def root_menu_service():
    root_menu_items = MenuItem.objects.filter(parent__isnull=True)

    return root_menu_items
