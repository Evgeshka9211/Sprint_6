import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:

    @allure.title('Проверяем форму заказа с кнопки в шапке страницы')
    def test_create_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.get_main_page()
        main_page.click_header_order_button()
        order_page.set_name("Фёдор")
        order_page.set_last_name("Конюхов")
        order_page.set_address("г.Москва, ул.Академика Королева, дом.12")
        order_page.set_metro_station()
        order_page.set_telephone_number("88005555555")
        order_page.click_cookie_button()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_period()
        order_page.set_color_black()
        order_page.set_color_grey()
        order_page.set_comment("Приду еще")
        order_page.click_order_button()
        order_page.click_modal_order_button()
        success_text = order_page.get_success_text()
        assert "Заказ оформлен" in success_text

    @allure.title('Проверяем форму заказа с кнопки внизу страницы')
    def test_create_order_from_bottom(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.get_main_page()
        main_page.click_middle_order_button()
        order_page.set_name("Миклухо")
        order_page.set_last_name("Маклай")
        order_page.set_address("г.Москва,ул.Садовая,д.12")
        order_page.set_metro_station()
        order_page.set_telephone_number("88007555545")
        order_page.click_cookie_button()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_period()
        order_page.set_color_black()
        order_page.set_comment("Приду снова")
        order_page.click_order_button()
        order_page.click_modal_order_button()
        success_text = order_page.get_success_text()
        assert "Заказ оформлен" in success_text