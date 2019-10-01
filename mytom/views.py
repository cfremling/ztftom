from django.views.generic import TemplateView
from tom_observations.models import Target
from tom_targets.views import TargetListView

class MyCustomTargetListView(TargetListView):
    template_name = 'mysupertargetlist.html'
    paginate_by = 100

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        return {'targets': Target.objects.all()}
