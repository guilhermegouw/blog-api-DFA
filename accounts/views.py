from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(csrf_exempt, name="dispatch")
class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Login View Hit!!!")
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login successful."})
        else:
            return Response(
                {
                    "non_field_errors": [
                        "Unable to log in with provided credentials."
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
