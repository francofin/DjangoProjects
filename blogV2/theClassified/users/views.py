from django.shortcuts import render
from .models import CustomUser, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, SignUpSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from requests import get
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets, parsers
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from jobs.validators import validate_image, validate_file_extension
# Create your views here.


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class  = UserSerializer

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

class UserProfileViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class  = UserProfileSerializer

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = UserSerializer(request.user)
    print(user) 

    return Response(user.data)



@api_view(['PUT', 'POST'])
@permission_classes([IsAuthenticated])
def update_user(request):

    user = request.user
    data = request.data
    profile_picture = request.FILES['profile_picture']

    is_valid_image = validate_image(profile_picture.name)
    print(is_valid_image)
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']
    user.userprofile.profile_picture = profile_picture

    if data['password'] != '':
        user.password = make_password(data['password'])
    
    if request.FILES['profile_picture'] != user.userprofile.profile_picture:
            user.userprofile.profile_picture = request.FILES['profile_picture']
    user.save()
    user.userprofile.save()

    serializer = UserSerializer(user, many=False)
    serializer_profile = UserProfileSerializer(user, many=False)
    if serializer.is_valid():
        serializer.save()

    if serializer_profile.is_valid():
        serializer_profile.save()

    return Response(serializer.data, serializer_profile.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)
    print(user)

    if user.is_valid():
        if not CustomUser.objects.filter(email=data['email']).exists():
            if data['password'] == data['password2']:
                user = CustomUser.objects.create(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    username = data['email'],
                    email = data['email'],
                    password = make_password(data['password'])
                )
                return Response({
                    'message':'User has been Registered'},
                    status = status.HTTP_200_OK)
            else:
                return Response({
                    'error':'Your Passwords Do not match please try again'},
                    status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                    'error':'User already Exist'},
                    status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors)

# class UserSignUpViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = SignUpSerializer
#     parser_classes = [parsers.MultiPartParser, parsers.FormParser]

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         user = SignUpSerializer(data=data)
#         if user.is_valid():
#             if not CustomUser.objects.filter(email=data['email']).exists():
#                 if data['password'] == data['password2']:
#                     user = CustomUser.objects.create(
#                         first_name = data['first_name'],
#                         last_name = data['last_name'],
#                         username = data['email'],
#                         email = data['email'],
#                         password = make_password(data['password']),
#                     )
#                     return Response({
#                         'message':'User has been Registered'},
#                         status = status.HTTP_200_OK)
#                 else:
#                     return Response({
#                         'error':'Your Passwords Do not match please try again'},
#                         status = status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response({
#                         'error':'User already Exist'},
#                         status = status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(user.errors)
    

# @api_view(['POST'])
# def register(request):
#     data = request.data
#     user = SignUpSerializer(data=data)
#     print(user)

#     if user.is_valid():
#         if not CustomUser.objects.filter(email=data['email']).exists():
#             if data['password'] == data['password2']:
#                 user = CustomUser.objects.create(
#                     first_name = data['first_name'],
#                     last_name = data['last_name'],
#                     username = data['email'],
#                     email = data['email'],
#                     password = make_password(data['password'])
#                 )
#                 return Response({
#                     'message':'User has been Registered'},
#                     status = status.HTTP_200_OK)
#             else:
#                 return Response({
#                     'error':'Your Passwords Do not match please try again'},
#                     status = status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({
#                     'error':'User already Exist'},
#                     status = status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(user.errors)

# @api_view(['GET'])
# def get_all_users(request):
#     if request.method == 'GET':
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)

#         return Response(serializer.data)


