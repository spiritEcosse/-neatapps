__author__ = 'igor'
from django.test import TestCase
from django.test import Client
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver


class NeatappsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_available_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class NeatappsJqueryTests(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(NeatappsJqueryTests, self).setUp()

    def tearDown(self):
        # call tearDown to close the web browser
        self.selenium.quit()
        super(NeatappsJqueryTests, self).tearDown()

    def test_slider(self):
        self.selenium.get(self.live_server_url)
        pages = self.selenium.find_element_by_class_name('camera_pag_ul').find_elements_by_tag_name('li')

        for page in pages:
            page.find_element_by_tag_name('span').click()

    def test_head_menu(self):
        self.selenium.get(self.live_server_url)
        links = self.selenium.find_element_by_id('menu').find_elements_by_tag_name('a')
        click = 0

        for link in links:
            link.click()
            click += 1
            element = link.get_attribute('href').split('#')[1]
            self.assertEqual(True, self.selenium.find_element_by_id(element).is_enabled())
            position_custom_scroll = self.selenium.execute_script("document.body.scrollTop;")
            self.selenium.execute_script("return arguments[0].scrollIntoView();",
                                         self.selenium.find_element_by_id(element))
            position_auto_scroll = self.selenium.execute_script("document.body.scrollTop;")
            self.assertEqual(position_custom_scroll, position_auto_scroll)

        self.assertEqual(click, len(links))


class AdminTestCase(LiveServerTestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com')

        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )

        # Fill login information of admin
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")

        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/admin/auth/user/add/")
        )

        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_username").send_keys("test")
        self.selenium.find_element_by_id("id_password1").send_keys("test")
        self.selenium.find_element_by_id("id_password2").send_keys("test")

        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_id("user_form").submit()
        self.assertIn("Change user", self.selenium.title)
