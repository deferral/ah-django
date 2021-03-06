import json

from rest_framework import renderers


class FollowerJsonRenderer(renderers.BaseRenderer):
    """
    List of followed users renderer
    """
    media_type = 'application/json'
    format = 'json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None,
               renderer_context=None):
        """
        List of followers renderer
        """
        if isinstance(data, list):
            return json.dumps(
                {'following': data})
        else:
            """
            Render a single follower or an error message
            """
            error = data.get('detail')
            if error:
                return json.dumps({'message': data})

            return json.dumps({'detail': data})


class FollowerListJsonRenderer(renderers.BaseRenderer):
    """
    Renders a list of followed users
    """
    media_type = 'application/json'
    format = 'json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None,
               renderer_context=None):
        """
        Render a list of followers
        """
        if isinstance(data, list):
            return json.dumps(
                {'followers': data})
        else:
            """
            Render a single follower or an error message
            """
            error = data.get('detail')
            if error:
                return json.dumps({'message': data})

            return json.dumps({'detail': data})
