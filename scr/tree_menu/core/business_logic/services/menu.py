from core.models import MenuItem
from typing import List


def root_menu_service() -> List[MenuItem]:
    root_menu_items = MenuItem.objects.filter(parent__isnull=True).all()
    return root_menu_items
