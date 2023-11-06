from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MyApiView(APIView):
    def get(self, request):
        data = {'message': 'Bnj, test API endpoint from bot manager app'}
        return Response(data)
