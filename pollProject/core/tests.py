from django.test import TestCase

from django.test.client import RequestFactory
from django.urls.base import reverse
from core.models import *
from core.views import *


class PollListPaginationTest(TestCase):

    ACTIVE_PAGINATION_HTML = """
    <li class="page-item.active">
    <a href="{}?page={}" class="page-link">{}</a>
    </li>
    """

    def setUp(self):
        for n in range(15):
            Poll.objects.create(
                title='Title {}'.format(n),
                description='Description {}'.format(n),
            )

    def testFirstPage(self):
        poll_list_path = reverse('core:PollList')
        request = RequestFactory().get(path=poll_list_path)
        response = PollList.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                poll_list_path, 1, 1),
            response.rendered_content)


