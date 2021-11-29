from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, request
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import employee,student
from .serializers import EmployeeSerializer, studentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.


#Function Based API

# @csrf_exempt
@api_view(['GET','POST'])
def employee_list(request):

    if request.method == 'GET':
        emp = employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data= JSONParser().parse(request)
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['GET','PUT','DELETE'])
def employee_details(request,pk):
    try:
        emp = employee.objects.get(pk=pk)

    except employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data  = JSONParser().parse(request)
        serializer = EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =="DELETE":
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Class Based API


class StudentAPIView(APIView):

    def get(self,request):
        students = student.objects.all()
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = studentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class studentdetails(APIView):

    def get_object(self,id):
        try:
            return student.objects.get(id=id)

        except student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        students = self.get_object(id)
        serializer = studentSerializer(students)
        return Response(serializer.data)

    def put(self,request,id):
        students = self.get_object(id)
        serializer = studentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        students = self.get_object(id)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#generics based view  


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = studentSerializer
    queryset = student.objects.all()

    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication,BaseAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)


# viewsets   code

class studentViewSet(viewsets.ViewSet):
    def list(self,request):
        students = student.objects.all()
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = studentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = student.objects.all()
        students = get_object_or_404(queryset,pk=pk)
        serializer = studentSerializer(students)
        return Response(serializer.data)

    def update(self,request,pk=None):
        students = student.objects.get(pk=pk)
        serializer = studentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
#generic viewset

class studentgenericviewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = studentSerializer
    queryset = student.objects.all()


#model viewset

class  stuModelciewset(viewsets.ModelViewSet):
    serializer_class = studentSerializer
    queryset = student.objects.all()