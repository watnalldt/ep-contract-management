from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("pages:home"))
        self.assertTemplateUsed(response, "pages/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "<p>This content needs replacing</p>")
        self.assertNotContains(response, "Not on the page")
