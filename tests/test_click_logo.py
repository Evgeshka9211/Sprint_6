import allure

from pages.main_page import MainPage
from constants import Urls
from constants import Texts

class TestLogo:

    @allure.title('Проверяем нажатие на логотип "Самокат"')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)

        main_page.get_main_page()
        main_page.click_header_scooter_logo()

        assert main_page.driver.current_url == Urls.scooter_main_page

    @allure.title('Проверяем нажатие на логотип "Яндекс"')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.get_main_page()
        main_page.click_header_yandex_logo()
        main_page.driver.switch_to.window(main_page.driver.window_handles[1])
        main_page.wait_until_page_loaded(Texts.dzen_page_title)
        assert main_page.driver.current_url == Urls.dzen_main_page or main_page.driver.current_url == f"{Urls.dzen_main_page}/"