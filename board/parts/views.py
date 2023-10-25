from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .forms import AdsForm
from .models import Ads
from .filters import AdsFilter



class AdsDetail(DetailView):
    model = Ads
    template_name = "ad.html"
    context_object_name = 'ad'

    """def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}',None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}',obj)
        return obj"""

class AdsSearch(ListView):
    model = Ads
    ordering = '-time_in'
    template_name = 'ads.html'
    context_object_name = 'ads_list'
    paginate_by = 10


    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AdsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context

# Добавляем новое представление для создания товаров.

class AdsCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('parts.add_ad',)

    form_class = AdsForm
    context_object_name = 'ads_create'
    model = Ads
    template_name = 'ads_edit.html'
    success_url = reverse_lazy('ads_list')


class AdsUpdate(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = ('parts.change_ad',)
    context_object_name = 'ads_create'
    form_class = AdsForm
    model = Ads
    template_name = 'ads_edit.html'
    success_url = reverse_lazy('ads_list')




class AdsDelete(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = ('parts.delete_ad',)
    model = Ads
    context_object_name = 'ads_delete'
    template_name = 'ads_delete.html'
    success_url = reverse_lazy('ads_list')

