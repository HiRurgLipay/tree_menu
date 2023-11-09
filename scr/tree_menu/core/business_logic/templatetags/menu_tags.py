from django import template
from core.models.menu import MenuItem
from typing import Union

register = template.Library()

@register.simple_tag
def build_menu(menu_items: Union[list, MenuItem], current_path: str) -> str:
    return render_menu(menu_items, current_path)

def render_menu(menu_items: Union[list, MenuItem], current_path: str) -> str:
    menu_html = ""

    for item in menu_items:
        submenu_items = MenuItem.objects.filter(parent=item)
        submenu_html = render_menu(submenu_items, current_path) if submenu_items else ""
        active = "active" if current_path == item.url else ""
        menu_html += f"""
            <li class='{active}'>
                <a href='{item.url}'>{item.title}</a>
                {submenu_html}
            </li>
        """
    return f"<ul>{menu_html}</ul>"
