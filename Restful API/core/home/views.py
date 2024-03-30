from rest_framework import viewsets, filters, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Paragraph
from .serializers import ParagraphSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['paragraph_name', 'paragraph_description']
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Simply delete the token or session for the user
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
