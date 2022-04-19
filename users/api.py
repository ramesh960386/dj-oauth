from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views import TokenView


class RegisterAPIView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'status':200,
                    'message': 'registration successfully check email',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'something went wrong',
                    'data': serializer.errors
                })
        except Exception as e:
            print(e)
            

# class LoginAPIView(APIView):
#     def post(self, request):
#         user = User.objects.filter(email=request.data['email']).first()

#         if not user:
#             raise APIException('Invalid credentials!')

#         if not user.check_password(request.data['password']):
#             raise APIException('Invalid credentials!')

#         access_token = create_access_token(user.id)
#         refresh_token = create_refresh_token(user.id)

#         response = Response()

#         response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
#         response.data = {
#             'token': access_token
#         }

#         return response


# class UserAPIView(APIView):
#     def get(self, request):
#         auth = get_authorization_header(request).split()

#         if auth and len(auth) == 2:
#             token = auth[1].decode('utf-8')
#             id = decode_access_token(token)

#             user = User.objects.filter(pk=id).first()

#             return Response(UserSerializer(user).data)

#         raise AuthenticationFailed('unauthenticated')


# class RefreshAPIView(APIView):
#     def post(self, request):
#         refresh_token = request.COOKIES.get('refreshToken')
#         id = decode_refresh_token(refresh_token)
#         access_token = create_access_token(id)
#         return Response({
#             'token': access_token
#         })


# class LogoutAPIView(APIView):
#     def post(self, _):
#         response = Response()
#         response.delete_cookie(key="refreshToken")
#         response.data = {
#             'message': 'success'
#         }
#         return response

@method_decorator(csrf_exempt, name="dispatch")
class TokenView(APIView):
    def post(self, request):
        return Response({'data':'fine'})
