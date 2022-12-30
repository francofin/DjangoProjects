from django.shortcuts import render, get_object_or_404
from .models import CustomUser, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, SignUpSerializer
from django.http import JsonResponse
from django.conf import settings
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
from utils.uploadImages import ImageUploader
from stockuploader.models import ProfileStock, Stock
from fintank_screener.serializers import ProfileSerializer
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

def get_payment_key(request):

    stripe_payment_key = settings.STRIPE_SECRET_KEY

    return Response(stripe_payment_key)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = UserSerializer(request.user)
    print(user) 

    return Response(user.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user_profile(request):
    user_profile = UserProfileSerializer(request.user)
    print(user_profile) 

    return Response(user_profile.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_portfolio(request):
    args = {'user':request.user.id}
    portfolio_stocks = ProfileStock.objects.filter(**args)
    serializer = ProfileSerializer(portfolio_stocks, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_stock_to_watchlist(request, ticker):
    user = request.user
    symbol = ticker
    stock = get_object_or_404(Stock, symbol=ticker)

    
    already_on_watchlist = stock.profilestock_set.filter(user=user).exists()
    if already_on_watchlist:
        return Response({
            'error':"You Have Already Added This Stock To Your WatchList"
        }, status = status.HTTP_400_BAD_REQUEST)

    portfolio_stock = ProfileStock.objects.create(
        symbol=symbol,
        user=user,
        stock = stock
    )

    serializer = ProfileSerializer(portfolio_stock)

    context = {
        'added':True,
        'stock':portfolio_stock.id
    }

    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_on_watch_list(request, ticker):
    user = request.user
    stock = get_object_or_404(Stock, symbol=ticker)

    applied = stock.profilestock_set.filter(user=user).exists()

    return Response(applied)

@api_view(['PUT', 'POST'])
@permission_classes([IsAuthenticated])
def update_user(request):

    user = request.user
    data = request.data
    print("Request", request.data)    

    # profile_picture = request.FILES["profile_picture"]
    

    # is_valid_image = validate_image(profile_picture.name)
    # print(is_valid_image)
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    # user.username = data['username']
    user.email = data['email']
    user.profile_picture_cs = data['profile_picture_cs']
    # ret = ImageUploader.UploadImage(user.first_name, profile_picture)

    

    if data['password'] != '':
        user.password = make_password(data['password'])

    # user.profile_picture = profile_picture
    
    # if request.FILES['profile_picture'] != user.profile_picture:

    user.save()

    serializer = UserSerializer(user, many=False, data=data)

    
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT', 'POST'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):

    user = request.user
    data = request.data

    user.userprofile.address = data['address']
    user.userprofile.date_of_birth = data['date_of_birth']
    user.userprofile.about = data['about']
    user.userprofile.about1 = data['about1']
    user.userprofile.about2 = data['about2']
    user.userprofile.about3 = data['about3']
    user.userprofile.about4 = data['about4']
    user.userprofile.about5 = data['about5']
    user.userprofile.about6 = data['about6']
    user.userprofile.about7 = data['about7']
    user.userprofile.about8 = data['about8']
    user.userprofile.about9 = data['about9']
    user.userprofile.about10 = data['about10']
    user.userprofile.about11 = data['about11']
    user.userprofile.about12 = data['about12']
    user.userprofile.about13 = data['about13']
    user.userprofile.about14 = data['about14']
    user.userprofile.cover_picture = data['cover_picture']
    user.userprofile.phone_number = data['phone_number']
    user.userprofile.profile_picture1 = data['profile_picture1']
    user.userprofile.profile_picture2 = data['profile_picture2']
    user.userprofile.profile_picture3 = data['profile_picture3']
    user.userprofile.profile_picture4 = data['profile_picture4']
    user.userprofile.profile_picture5 = data['profile_picture5']
    user.userprofile.profile_picture6 = data['profile_picture6']
    user.userprofile.profile_picture7 = data['profile_picture7']
    user.userprofile.profile_picture8 = data['profile_picture8']
    user.userprofile.profile_picture9 = data['profile_picture9']
    user.userprofile.profile_picture10 = data['profile_picture10']
    user.userprofile.resume = data['resume']
    user.userprofile.document = data['document']
    user.userprofile.document1 = data['document1']
    user.userprofile.document2 = data['document2']
    user.userprofile.document3 = data['document3']
    user.userprofile.document4 = data['document4']
    user.userprofile.stripe_account_id = data['stripe_account_id']

    user.userprofile.save()

    serializer = UserSerializer(user, many=False, data=data)

    
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data, status=status.HTTP_200_OK)


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


