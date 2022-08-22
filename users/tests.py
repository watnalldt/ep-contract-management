from django.contrib.auth import get_user_model
from django.test import TestCase


class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            "testuser@super.com", "Super User", "password"
        )
        self.assertEqual(super_user.email, "testuser@super.com")
        self.assertEqual(super_user.name, "Super User")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testuser@super.com")
        self.assertEqual(super_user.short_name, "Super")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                name="Super User",
                password="password",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                name="Super User",
                password="password",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="", name="Super User", password="password", is_superuser=True
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            "testuser@user.com",
            "Alice Smith",
            "password",
        )
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.name, "Alice Smith")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_account_manager)

        with self.assertRaises(ValueError):
            db.objects.create_user(email="", name="a", password="password")
