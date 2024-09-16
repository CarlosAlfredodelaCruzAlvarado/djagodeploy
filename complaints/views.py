from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint, Comment
from .forms import ComplaintForm
from rest_framework import viewsets
from .serializers import ComplaintSerializer, CommentSerializer
from rest_framework.decorators import action  # Import the action decorator
from rest_framework.response import Response
from django.http import JsonResponse

# Vista de la API para el conjunto de datos de Complaint
class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

# Vista personalizada para obtener complaints como JSON
def get_complaints(request):
    complaints = Complaint.objects.all().values()  # Obtén todos los complaints como un queryset de diccionarios
    return JsonResponse(list(complaints), safe=False)  # Envía los datos en formato JSON

# Vista para listar todos los complaints en una página HTML
def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

# Vista para los detalles de un complaint en una página HTML
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    comments = complaint.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.complaint = complaint
            comment.save()
            return redirect('complaint_detail', pk=complaint.pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'complaints/complaint_detail.html', {
        'complaint': complaint,
        'comments': comments,
        'comment_form': comment_form
    })

# Vista para crear un nuevo complaint
def complaint_create(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_form.html', {'form': form})

# CommentViewSet with a custom action
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['get'])
    def by_complaint(self, request):
        complaint_id = request.query_params.get('complaint')
        if complaint_id:
            comments = self.queryset.filter(complaint_id=complaint_id)
            serializer = self.get_serializer(comments, many=True)
            return Response(serializer.data)
        return Response([])  # Return an empty list if no complaint_id is provided