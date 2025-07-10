from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group  # ✅ import auth models
from django.contrib.auth.admin import UserAdmin, GroupAdmin  # ✅ import admin configs

from .models import Item  # your custom model


class MyAdminSite(AdminSite):
    site_header = "Inventory Dashboard"
    site_title = "Inventory Admin Portal"
    index_title = "Welcome to Inventory Dashboard"

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }
        js = ('js/admin_ui.js',) 


# ✅ create custom_admin_site instance
custom_admin_site = MyAdminSite(name='custom_admin')

# ✅ Register custom models and auth models
custom_admin_site.register(Item)
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)

class MyAdminSite(AdminSite):
    site_header = "Inventory Dashboard"
    site_title = "Inventory Admin"
    index_title = "Welcome to Inventory Dashboard"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_admin.css'
        return context

admin_site = MyAdminSite(name='myadmin')

