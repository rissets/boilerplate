from django.http import request
from django.shortcuts import render
from django.views import View


# Vertical Layouts
# Light Sidebar
class LightSidebarView(View):
    def get(self, request):
        greeting = {'title': "Light SIdebar", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-light-sidebar.html',greeting)


# Compact Sidebar
class CompactSidebarView(View):
    def get(self, request):
        greeting = {'title': "Compact Sidebar", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-compact-sidebar.html',greeting)


# Icon SIdebar
class IconSidebarView(View):
    def get(self, request):
        greeting = {'title': "Icon Sidebar", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-icon-sidebar.html',greeting)


# Boxed Layout
class BoxedLayoutView(View):
    def get(self, request):
        greeting = {'title': "Boxed Layout", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-boxed.html',greeting)


# Preloader Layout
class PreloaderLayoutView(View):
    def get(self, request):
        greeting = {'title': "Preloader", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-preloader.html',greeting)


# Colored Sidebar
class ColoredSidebarView(View):
    def get(self, request):
        greeting = {'title': "Colored Sidebar", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/vertical/layouts-colored-sidebar.html',greeting)

# # Vertical Scrollable
# class VerticalScrollableView(View):
#     def get(self, request):
#         greeting = {}
#         greeting['title'] = "Vertical Scrollable"
#         greeting['pageview'] = "Layouts"        
#         return render(request, 'menu/layouts/vertical/layouts-scrollable.html',greeting)        


# Horizontal Layouts
# Horizontal Layout
class HorizontalView(View):
    def get(self, request):
        greeting = {'title': "Horizontal", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/horizontal/layouts-horizontal.html',greeting)


# Light Topbar
class TopbarLightView(View):
    def get(self, request):
        greeting = {'title': "Topbar Light", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/horizontal/layouts-hori-topbar-light.html',greeting)


# Boxed Width
class BoxedWidthView(View):
    def get(self, request):
        greeting = {'title': "Boxed Width", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/horizontal/layouts-hori-boxed-width.html',greeting)


# Preloader Layout
class HorizontalPreloaderLayoutView(View):
    def get(self, request):
        greeting = {'title': "Horizontal Preloader Layout", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/horizontal/layouts-hori-preloader.html',greeting)


# Colored Header
class ColoredHeaderView(View):
    def get(self, request):
        greeting = {'title': "Colored Header", 'pageview': "Layouts"}
        return render(request, 'menu/layouts/horizontal/layouts-hori-colored-header.html',greeting)

# # Horizontal Scrollable
# class HorizontalScrollableView(View):
#     def get(self, request):
#         greeting = {}
#         greeting['title'] = "Horizontal Scrollable"
#         greeting['pageview'] = "Layouts"        
#         return render(request, 'menu/layouts/horizontal/layouts-hori-scrollable.html',greeting)
