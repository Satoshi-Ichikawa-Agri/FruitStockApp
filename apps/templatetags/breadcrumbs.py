from django import template
from django.urls import resolve

register = template.Library()


@register.simple_tag
def breadcrumbs(request):
    path = request.path
    url_names = path.strip("/").split("/")
    breadcrumb_trail = []

    for index, url_name in enumerate(url_names):
        url_path = "/".join(url_names[: index + 1])
        try:
            name = resolve("/" + url_path).url_name
            breadcrumb_trail.append((name, "/" + url_path))
        except:
            breadcrumb_trail.append((url_name, "/" + url_path))

    return breadcrumb_trail
