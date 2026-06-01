from django.test import TestCase


class PageTest(TestCase):

    def test_home_page(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_menu_page(self):

        response = self.client.get('/menu/')

        self.assertEqual(response.status_code, 200)

    def test_booking_page(self):

        response = self.client.get('/booking/')

        self.assertEqual(response.status_code, 200)