# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestJWTView(APIView):
    """Dummy view to test jwt authentication"""

    def get(self, request):
        # Dummy response
        return Response(data={'success': 'yes'}, status=200)
