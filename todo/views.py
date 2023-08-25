from datetime import timedelta
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Task
from .serializers import TaskSerializer

from .forms import TodoForm
from .tasks import send_task_reminder




# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/create-task /',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def CreateTask(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		print(serializer.data)

	return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['PUT'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data,partial=False)
   
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

#views for template

def index(request):
	item_list  = Task.objects.order_by("-due_date")
	if request.method == "POST":
		form =TodoForm(request.POST)
		if form.is_valid():
			task = form.save()
			reminder_time = task.reminder_time
			send_task_reminder.apply_async((task.id,), eta=reminder_time)
			return redirect('todo')
	else:
		form = TodoForm()
	
	page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    	}
	return render(request, 'todo/index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')





