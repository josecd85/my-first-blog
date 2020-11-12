from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
import logging
#Pildoras
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    #logging.debug('NRows result:'+ str(len(posts)))
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    #post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk) 
            #return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment.html', {'form':form})

@login_required
def comment_ok(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("post_detail", pk=comment.post.pk)
    
@login_required
def comment_del(request, pk):
    cmm = get_object_or_404(Comment, pk=pk)
    cmm.delete()
    return redirect("post_detail", pk=cmm.post.pk)

def prueba1(request):
    return render(request, 'blog/prueba1.html', {})


#Pildoras
def cursoC (request):
    fecha_actual=datetime.datetime.now()

    return render (request, "pildoras/CursoC.html", {"dameFecha":fecha_actual})

def cursoDjango (request):
    fecha_actual=datetime.datetime.now()

    return render (request, "pildoras/CursoDjango.html", {"dameFecha":fecha_actual})

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    

def saludo (request):
    p1 = Persona("Jose", "Caballero")
    ahora=datetime.datetime.now()

    temasCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    # Forma 1
    # doc_externo=open("C:/virtualEnv/blog/templates/blog/pildoras.html")
    # plt=Template(doc_externo.read())
    # doc_externo.close()
    # ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasCurso})
    # documento=plt.render(ctx)
    # return HttpResponse(documento)
    
    # Forma 2
    # doc_externo=loader.get_template('pildoras.html')
    # documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasCurso})
    # return HttpResponse(documento)

    return render(request, "pildoras/pildoras.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasCurso})

def dameFecha (request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad (request, edad, agno):
    periodo=agno-2019
    edadFutura=edad+periodo
    documento="""
    <html>
    <body>
    <h1>
    En el año: %s tendrás %s años
    </h1>
    </body>
    </html>""" % (agno, edadFutura)

    return HttpResponse(documento)