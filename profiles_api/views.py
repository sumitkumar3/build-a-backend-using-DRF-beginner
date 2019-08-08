from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class HelloViewSet(viewsets.ViewSet):
    """test ApI viewset"""
    def list(self, request):
        """return a hello meassage"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'hello', 'hello-viewset': a_viewset})


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle create update user profile"""
    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =  (TokenAuthentication,)
    permission_classes = (permissions.UpadateOwnProfile, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
