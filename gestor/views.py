
# gestor/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import DocumentForm
from .models import Case, Document
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.title = document.file.name  # Establece el nombre del archivo como título
            document.save()
            return redirect('case-detail', pk = document.case.id)  # Redirige a una página de lista o detalle
    else:
        form = DocumentForm()
    return render(request, 'gestor/upload_document.html', {'form': form})
    
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('case-list')  # Redirige a la lista de casos si está autenticado
    else:
        return redirect('login')  # Redirige a login si no está autenticado

# Vista para listar todos los casos
def logout_view(request):
    logout(request)
    return redirect('login') 
    
class CaseListView(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'gestor/case_list.html'  # Archivo HTML para la lista de casos
    context_object_name = 'cases'  # Nombre de la variable en el contexto

# Vista para el detalle de un caso específico
class CaseDetailView(LoginRequiredMixin , DetailView):
    model = Case
    template_name = 'gestor/case_detail.html'  # Archivo HTML para el detalle de cada caso
    context_object_name = 'case'  # Nombre de la variable en el contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recupera los documentos relacionados con este caso
        context['documents'] = Document.objects.filter(case=self.object)
        return context

# Create your views here.
