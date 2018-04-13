from django.contrib.auth.backends import ModelBackend

from base import mods


class AuthBackend(ModelBackend):
    '''
    This class makes the login to the authentication method for the django
    admin web interface.

    If the content-type is x-www-form-urlencoded, a requests is done to the
    authentication method to get the user token and this token is stored
    for future admin queries.
    '''

    def authenticate(self, request, username=None, password=None, **kwargs):
        u = super().authenticate(request, username=username,
                                 password=password, **kwargs)

        # only doing this for the admin web interface
        if u and request.content_type == 'application/x-www-form-urlencoded':
            data = {
                'username': username,
                'password': password,
            }
            token = mods.post('authentication', entry_point='/login/', json=data)
            request.session['auth-token'] = token['token']

        return u
