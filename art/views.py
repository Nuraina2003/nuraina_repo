from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from .forms import *
from .models import *
from .utils import *



class artHome(DataMixin, ListView):
    model = art
    template_name = 'art/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return art.objects.filter(is_published=True)




# def index(request):
#     posts = art.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'art/index.html', context=context)

def about(request):
    contact_list = art.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'art/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'About site'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'art/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Page")
        return dict(list(context.items()) + list(c_def.items()))
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'art/addpage.html', { 'form': form, 'menu': menu, 'title': 'Add page'})

# def contact(request):
#     return HttpResponse("Contact")

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'art/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Contact")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# def login(request):
#     return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not found page</h1>')

# def show_post(request, post_slug):
#     post = get_object_or_404(art, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'art/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = art
    template_name = 'art/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class artCategory(DataMixin, ListView):
    model = art
    template_name = 'art/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return art.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = art.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Display by headings',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'art/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'art/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'art/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def registration(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'art/register.html',{'form': form,'title': 'registration'})


def send_message(request):
    send_mail('django test mail', 'this is django test body',
              '200103126@stu.sdu.edu.kz',
              ['200103126@stu.sdu.edu.kz','n060103@mail.ru'],
              fail_silently=False, html_message="<b>Bold text</b><i> Italic text</i>")
    return render(request, 'art/successfull.html')

def send_message(request):
    email = EmailMessage(
        'Hello',
        'Body goes here',
        '200103126@stu.sdu.edu.kz',
        ['200103126@stu.sdu.edu.kz', 'n060103@mail.ru'],
        headers={'Message-ID': 'foo'},

    )
    email.attach_file('/Users/Привет/Pictures/Screenshots/2.png')
    email.send(fail_silently=False)
    return render(request, 'art/successfull.html')
