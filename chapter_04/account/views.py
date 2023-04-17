from rest_framework.generics import CreateAPIView
from django.contrib.auth.hashers import make_password
from .models import Account
from .serializers import AccountSerializer


# Create your views here.
class SignUp(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data["password"])
        serializer.save(password=password)
