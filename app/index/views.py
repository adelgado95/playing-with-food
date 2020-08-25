from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)