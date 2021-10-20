from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse, render
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView

from app.forms import ContactForm, CommentForm, NewsletterForm
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = Seo.objects.all()
        context['about'] = About.objects.all()
        context['seo_team'] = SeoTeam.objects.all()
        context['plan'] = Plan.objects.all()
        context['blog'] = Blog.objects.all().order_by("-pk")[:3]
        context['section'] = HomeSection.objects.all()
        context['banner_section'] = BannerSection.objects.all()
        context['sub_banner'] = SubBanner.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan'] = Plan.objects.all()
        context['about'] = About.objects.all()
        return context


class ServicesView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = Seo.objects.all()
        context['seo_team'] = SeoTeam.objects.all()
        return context


# class BlogView(TemplateView):
#     template_name = 'blog.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['blog'] = Blog.objects.all()
#         context['category'] = Category.objects.all()
#         return context
class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'blog.html'
    paginate_by = 6

    # paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = Paginator(Blog.objects.select_related().all(), self.paginate_by)
        context['blog'] = p.page(context['page_obj'].number)
        # context['blog'] = Blog.objects.all()
        context['category'] = Category.objects.all()
        return context


class ContactUs(TemplateView):
    template_name = 'contact.html'


class BlogDetailsView(TemplateView):
    template_name = 'blog-details.html'


class ContactusView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('contact_us'))


class CommentView(CreateView):
    template_name = 'blog-details.html'
    form_class = CommentForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('leave_comment'))


class NewsletterView(CreateView):
    template_name = 'footer.html'
    form_class = NewsletterForm

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('index'))


# def detail(request, question_id):
#     try:
#         question = Blog.objects.get(pk=question_id)
#     except Blog.DoesNotExist:
#         raise Http404("Soryy  no any blog")
#     return render(request, 'blog-details.html', {'question': question})

class Detail(generic.DetailView):
    model = Blog
    template_name = 'blog-details.html'

    # def get(self, request, *args, **kwargs):
    #     pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs['pk']
        context['blog'] = Blog.objects.filter(id=blog_id)
        context['blogs'] = Blog.objects.all().order_by("-pk")[:3]
        # context['category'] = Category.objects.all()
        return context


# def search(request):
#     qur = request.GET.get('search')
#     cat = Blog.objects.filter(title__contains=qur)
#     return render(request, 'blog-details.html', {"cat": cat})


class CategoryView(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'blog.html'
    model = Blog
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        context['category'] = Category.objects.all()
        # context['blog'] = Blog.objects.filter(category_id=category_id)
        p = Paginator(Blog.objects.select_related().filter(category_id=category_id), self.paginate_by)
        context['blog'] = p.page(context['page_obj'].number)

        return context

class SearchView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            # postresult = Doctors.objects.filter(department__contains=query)
            doctor = [item for item in Blog.objects.all() if query in item.description or query in item.title]
            result = doctor
        else:
            result = None
        return result
