from http import HTTPStatus

from django.test import Client, TestCase

urls_content = (
    ('/', 'У меня получилось!')
    ('/second_page/', 'А это вторая страница')
)


class StaticPagesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        for url, _ in urls_content:
            response = self.guest_client.get(url)
            self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        for url, content in urls_content:
            response = self.guest_client.get(url)
            self.assertContains(response, content)
