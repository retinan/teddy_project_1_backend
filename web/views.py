from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def main(request):
#     print(request.GET)
#     context = {
#         'data': {
#             'get_host': request.get_host,
#             'path': request.path,
#             'method': request.method,
#             'user': request.user,
#         }
#     }
#     return render(request, 'main.html', context=context)


class Main(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = {
            'get_host': self.request.get_host,
            'path': self.request.path,
            'method': self.request.method,
            'user': self.request.user,
        }
        return context


class HomeView(TemplateView):
    template_name = 'home.html'