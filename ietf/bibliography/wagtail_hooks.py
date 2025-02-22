from django.urls import reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem


@hooks.register("register_admin_menu_item")
def register_references_menu_item():
    return MenuItem(
        "References",
        reverse("referenced_types"),
        classnames="icon icon-folder-inverse",
        order=10000,
    )
