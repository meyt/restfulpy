
import itsdangerous
from restfulpy.principal import JwtPrincipal
from restfulpy.orm import DBSession

from nanohttp import Controller, context, settings, json, RestController


class JwtController(Controller):
    token_key = 'HTTP_X_JWT_TOKEN'

    def begin_request(self):
        if self.token_key in context.environ:
            try:
                context.identity = JwtPrincipal.decode(context.environ[self.token_key])
            except itsdangerous.SignatureExpired:
                context.identity = None
        else:
            context.identity = None

    # noinspection PyMethodMayBeStatic
    def begin_response(self):
        if settings.debug:
            context.response_headers.add_header('Access-Control-Allow-Origin', '*')
            context.response_headers.add_header('Access-Control-Allow-Headers', 'Content-Type, x-jwt-token')

    # noinspection PyMethodMayBeStatic
    def end_response(self):
        DBSession.remove()

    def __call__(self, *remaining_paths):
        if context.method == 'options':
            context.response_headers.add_header("Cache-Control", "no-cache,no-store")
            return b''

        return super(JwtController, self).__call__(*remaining_paths)


class ModelRestController(RestController):
    __model__ = None

    @json
    def metadata(self):
        return self.__model__.json_metadata()
