from django.test import TestCase
from django.urls import reverse

from accounts.forms import SignupForm


class SignupFormTest(TestCase):
    def test_signup_form(self):
        form = SignupForm(
            {
                "name": "playhub",
                "email": "email@playhub.kr",
                "password1": "123password123",
                "password2": "123password123",
                "phone_0": "KR",
                "phone_1": "01028236601",
                "gender": "M",
            }
        )
        self.assertTrue(form.is_valid())

    def test_signup_view(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

        response = self.client.post(
            reverse("accounts:signup"),
            {
                "name": "playhub",
                "email": "email@playhub.kr",
                "password1": "123password123",
                "password2": "123password123",
                "phone_0": "KR",
                "phone_1": "01028236601",
                "gender": "M",
            },
        )

        self.assertEqual(response.status_code, 302)
