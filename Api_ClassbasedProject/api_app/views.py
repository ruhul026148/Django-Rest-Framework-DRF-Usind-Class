from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api_app.serializers import *
from api_app.models import *

# Create your views here.
class StudentCreateListApi(APIView):
    def get(self, request):
        student_data=StudentModel.objects.all()
        serializer=StudentSerializer(student_data, many=True)
        return Response({
            "success":True,
            "message":"Data reterived Successfully",
            "data":serializer.data
        })
    def post(self,request):
        serializer= StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success":True,
                "message":"Data created Successfully",
                "data":serializer.data
            })
        return Response({
            "success":False,
            "error":serializer.data
        })
    
class StudentDetailsApi(APIView):
    def get_data(self,pk):
        try:
            student_data=StudentModel.objects.get(id=pk)
            return student_data
        except:
            return Response({
            "success":False,
            "message":"Data Not Found",
        })


    def get(self, request,pk):

        student_data= self.get_data(pk)
        serializer=StudentSerializer(student_data)
        return Response({
            "success":True,
            "message":"Data get Successfully",
            "data":serializer.data
        })
    def put(self, request, pk):
        student_data = self.get_data(pk)
        serializer = StudentSerializer(student_data, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success":True,
                "message":"Data Update Successfully",
                "data":serializer.data
            })
        
    def patch(self, request, pk):
        student_data = self.get_data(pk)
        serializer = StudentSerializer(student_data, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success":True,
                "message":"Data Patch Successfully",
                "data":serializer.data
            })
        return Response({
                "success":False,
                "error":serializer.error
            })
        
    def delete(self, request, pk):
        self.get_data(pk).delete()
        return Response({
                "success":True,
                "message":"Data Delete Successfully",
            })

