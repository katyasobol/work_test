from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    menu_items = MenuItem.objects.filter(parent=None, name=menu_name).prefetch_related('children')
    return _render_menu_items(menu_items, current_url)

def _render_menu_items(menu_items, current_url):
    result = []
    for item in menu_items:
        is_active = current_url.startswith(item.url)
        children = item.children.all()
        has_children = children.exists()
        result.append({
            'name': item.name,
            'url': item.url,
            'is_active': is_active,
            'has_children': has_children,
            'children': _render_menu_items(children, current_url) if has_children else None
        })
    return result
