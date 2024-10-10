from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class IndexPageView(UserPassesTestMixin, TemplateView):
    template_name = 'app/index.html'

    def test_func(self):
        return self.request.user.is_anonymous or self.request.user.is_superuser

