# -*- coding: utf-8 -*-
"""
Views for base app
"""

from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render
from obp.forms import DirectLoginForm, GatewayLoginForm


class HomeView(TemplateView):
    """View for home page"""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'API_HOST': settings.API_HOST,
            'logo_url': settings.LOGO_URL,
            'override_css_url': settings.OVERRIDE_CSS_URL,
            'directlogin_form': DirectLoginForm(),
            'gatewaylogin_form': GatewayLoginForm(),
        })
        return context



