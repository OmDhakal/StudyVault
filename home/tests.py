from django.contrib.auth.models import User
from django.test import TestCase


class AuthenticationFeedbackTests(TestCase):
    def test_invalid_registration_renders_field_errors_and_submitted_values(self):
        response = self.client.post(
            "/register",
            {
                "username": "",
                "email": "not-an-email",
                "password1": "short",
                "password2": "different",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(response, "The two password fields didn’t match.")
        self.assertContains(response, "Registration failed.")
        self.assertIn("form", response.context)

    def test_successful_registration_redirects_with_success_message(self):
        response = self.client.post(
            "/register",
            {
                "username": "newstudent",
                "email": "student@example.com",
                "password1": "A-strong-password-123",
                "password2": "A-strong-password-123",
                "terms": "on",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [("/login", 302)])
        self.assertTrue(User.objects.filter(username="newstudent").exists())
        self.assertContains(response, "Registration successful. Please log in.")

    def test_invalid_login_renders_error_message(self):
        response = self.client.post(
            "/login",
            {"username": "missing-user", "password": "wrong-password"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password.")


class PrivatePageAccessTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student",
            email="student@example.com",
            password="A-strong-password-123",
        )

    def test_private_pages_redirect_anonymous_users_to_login(self):
        for path in ["/", "/resources", "/library", "/profile"]:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertRedirects(response, f"/login?next={path}")

    def test_auth_pages_redirect_authenticated_users_to_home(self):
        self.client.force_login(self.user)

        for path in ["/login", "/register"]:
            with self.subTest(path=path):
                self.assertRedirects(self.client.get(path), "/")

    def test_authenticated_pages_show_dashboard_navigation(self):
        self.client.force_login(self.user)
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard")
        self.assertContains(response, "My Library")
        self.assertContains(response, "Profile")
        self.assertContains(response, "Logout")
        self.assertNotContains(response, 'href="/login"')
        self.assertNotContains(response, 'href="/register"')

    def test_logout_returns_user_to_login(self):
        self.client.force_login(self.user)

        response = self.client.get("/logout", follow=True)

        self.assertRedirects(response, "/login")
        self.assertContains(response, "You have been logged out.")
