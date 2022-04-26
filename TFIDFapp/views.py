from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from TFIDFapp.forms import UploadFileForm, ComputeForm
from TFIDFapp.functions import compute_and_fill_db_tf, make_table, uniq_words, corpus
from TFIDFapp.models import AddFile, TF, IDF


class AddFileView(CreateView):
    model = AddFile
    form_class = UploadFileForm
    template_name = 'TFIDFapp/addfile.html'
    success_url = reverse_lazy('add_file')


def fill_db(request):
    '''Заполняет таблицы TF и IDF в БД'''
    try:
        compute_and_fill_db_tf()
    except:
        raise Http404("Необходимо очистить таблицы в БД!!!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def chose_file(request):
    '''Получаем от пользователя номер документа, для которого необходимо посчитать TF и строим таблицу'''
    if request.method == "POST":
        forma = ComputeForm(request.POST)
        if forma.is_valid():
            table = make_table(forma.cleaned_data['doc_number'])
            return render(request, 'TFIDFapp/Table.html', {'table': table})
    else:
        forma = ComputeForm()
        return render(request, 'TFIDFapp/chose-compute.html', {'form': forma})


class ClearAllView(View):
    '''Очищаем БД и '''
    def get(self, request):
        TF.objects.all().delete()
        IDF.objects.all().delete()
        uniq_words.clear()
        corpus.clear()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
