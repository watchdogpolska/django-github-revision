from django.template import engines, Template, Context
from django.test import TestCase
import mock

from github_revision.context_processors import github_revision


class ContextProcessorTestCase(TestCase):
    @mock.patch("github_revision.backends.dealer", lambda x=None: 'REV_TEST')
    def test_data_types(self):
        result = github_revision()
        self.assertIsInstance(result, dict)
        self.assertIn('github', result)
        self.assertIn('url', result['github'])
        self.assertIn('revision_id', result['github'])


class TemplateTagsTestCase(TestCase):
    @mock.patch("github_revision.backends.dealer", lambda x=None: 'REV_TEST')
    def test_render_html(self):
        template = Template("{% load github_revision_tags %}{% github_link %}")
        content = template.render(Context())
        self.assertEqual(content,
                         '<a href="https://github.com/watchdogpolska/django-github-revision/compare/'
                         'REV_TEST...master">REV_TES</a>')