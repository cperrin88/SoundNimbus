from actstream import action
from actstream.models import user_stream
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView

from profiles.forms import PostForm


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_stream'] = user_stream(self.request.user, with_user_activity=True).filter(verb="posted")
        context['post_form'] = PostForm()
        return context


class PostView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request):
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post_model = post.save()
            action.send(request.user, verb='posted', action_object=post_model)
            return HttpResponseRedirect('/profiles')
