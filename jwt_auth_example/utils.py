from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication


class CustomJSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    """Extends BaseJSONWebTokenAuthentication in django-rest-framework-jwt.

    C.f. http://getblimp.github.io/django-rest-framework-jwt
    """

    def get_jwt_value(self, request):
        """Specifies that the jwt token should be passed via GET parameters, instead of the Authenticate header."""

        return request.query_params.get('jwt')
