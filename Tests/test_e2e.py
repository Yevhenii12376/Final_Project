import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_e2e(page):
    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_label("E-mail").click()
    page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
    page.get_by_label("E-mail").press("Tab")
    page.get_by_placeholder("Пароль").fill("13052000n")
    page.get_by_placeholder("Пароль").press("Enter")
    page.get_by_role("link", name="Парфумерія", exact=True).click()
    page.goto("https://makeup.com.ua/ua/product/977/")
    page.get_by_title("В обране").click()
    page.locator("#popup__window").get_by_text("Не спостерігати за зміною ціни").click()
    page.get_by_role("link", name="2", exact=True).click()
    page.locator(".product__remove-button").first.click()
    page.get_by_text("Купити").nth(1).click()
    # Перевірка сторінки Оформлення замовлення
    page.get_by_text("Оформити замовлення").click()
    page.get_by_role("link", name="MAKEUP").click()
    # Перевірка сторінки Доставка та оплата
    page.get_by_role("link", name="Доставка та Оплата").click()
    # Перевірка сторінки Про нас
    page.get_by_role("link", name="Про нас").click()
    page.goto("https://makeup.com.ua/ua/articles/")
    # Перевірка сторінки Акції
    page.get_by_role("link", name="Акції").click()
    # Перевірка сторінки Про магазин
    page.get_by_role("link", name="Про магазин").click()
    page.locator(".header-basket").click()
    page.locator(".header-office").click()
    page.get_by_role("link", name="Вихід").click()

def test_product_search(page):

    page.goto("https://makeup.com.ua/ua/")
    # Перевірка кнопки пошуку товару
    page.locator(".search-button").first.click()
    # Перевірка пошуку товару
    page.get_by_placeholder("Понад 249 000 товарів").fill("крем для рук")
    page.get_by_placeholder("Понад 249 000 товарів").press("Enter")
    page.goto("https://makeup.com.ua/ua/product/32739/")

def test_filter_check(page):

    page.goto("https://makeup.com.ua/ua/")
    # Перехід на сторінку Тіло і ванна
    page.get_by_role("link", name="Тіло і ванна").click()
    page.locator("#popularinput-checkbox-2243-29953").click()
    # Перехід на товар
    page.goto("https://makeup.com.ua/ua/categorys/321073/#o[2243][]=29953")

def test_password_change_verification(page):
    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_text("Забули пароль?").click()
    page.wait_for_timeout(1500)
    page.get_by_role("textbox", name="E-mail").click()
    page.get_by_role("textbox", name="E-mail").fill("o.ionenko129@gmail.com")
    page.get_by_role("button", name="Нагадати").click()
    page.locator("#popup__window div").first.click()

def test_email_change_verification(page):

    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
    page.get_by_role("button", name="Увійти").click()

def test_verification_without_login(page):

    page.goto("https://makeup.com.ua/ua/")
    page.locator(".header-office").click()
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("13052000n")
    page.get_by_role("button", name="Увійти").click()


if __name__ == "__main__":
  pytest.main([__file__])

