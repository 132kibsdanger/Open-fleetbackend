from django.shortcuts import render
from .models import CustomUser, Access_level, Vehicle, Tyre, Fault, Service_schedule, Maintenance_type,Work_order,Maintenance_record,Staff,Garage,Garage_manager
from .serializers import CustomUserSerializer, Access_levelSerializer, VehicleSerializer, TyreSerializer, FaultSerializer, Service_scheduleSerializer, Maintenance_typeSerializer,Work_orderSerializer,Maintenance_recordSerializer,StaffSerializer,GarageSerializer,Garage_managerSerializer
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
# Here are the API endpoints for the accounts app

class Register(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else:
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


