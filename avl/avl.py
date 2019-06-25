# -*- coding: utf-8 -*-

"""Main module."""

import requests

from . import settings


class Lab(object):
    FIELDS = ('pk', 'planned_expiration_time')
    READ_ONLY_FIELDS = ('pk',)
    PATCH_FIELDS = ('planned_expiration_time',)

    def __init__(self, pk):
        self.pk = pk
        self.headers = {
            'Authorization': 'Token {}'.format(settings.AVL_API_TOKEN)
        }

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "avl.avl.Lab(pk={})".format(self.pk)

    @property
    def response(self):
        msg = "You must make a request before the response is available."
        assert self._response, msg

        return self._response

    def _serialize_response(self, response):
        self._response = response

        return self

    def json(self):
        """Take a raw JSON string and update this object, then
        return it."""
        self._response.json()

    def _patch(self, data):
        path = '/isc/dashboard/userprojectdeployments/{pk}/'

        response = requests.patch(
            # TODO: Use urllib to build this url.
            '{}/{}'.format(settings.AVL_DOMAIN, path.format(pk=self.pk)),
            headers=self.headers,
            data=data
        )

        return response

    def patch(self, data):
        for field in data.keys():
            msg = "This field cannot be patched: {}."
            if field not in self.READ_ONLY_FIELDS:
                assert field in self.PATCH_FIELDS, msg.format(field)

        return self._serialize_response(self._patch(data))
