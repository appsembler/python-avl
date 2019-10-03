#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `avl` package."""

import datetime
import simplejson as json
from pathlib import Path

import pytest

from click.testing import CliRunner

from avl import avl
from avl import cli


class ResponseMock(object):
    def __init__(self):
        self.ok = True
        self.status_code = 200
        self.response = ResponseMock

    def json(self):
        patch_fixture_filepath = Path('.') / 'tests' / 'avl_patch_response_fixture.json'  # noqa: E501
        with patch_fixture_filepath.open('r+') as f:
            return json.loads(f.read())


class LabMock(object):

    def __init__(self):
        self.response = ResponseMock


@pytest.fixture
def response():
    """
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

    return ResponseMock()


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'avl.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_patch_lab(response):
    lab = avl.Lab(pk=38)
    lab._response = response
    lab._patch = lambda x: response

    update_to = datetime.datetime.today() + datetime.timedelta(days=14)
    data = {'planned_expiration_time': update_to}

    lab = lab.patch(data)

    assert lab.response.ok
    assert lab.response.status_code == 200

    patch_fixture_filepath = Path('.') / 'tests' / 'avl_patch_response_fixture.json'  # noqa: E501
    with patch_fixture_filepath.open('r+') as f:
        assert lab.response.json()['planned_expiration_time'] == \
            json.loads(f.read())['planned_expiration_time']
