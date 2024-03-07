from playwright.sync_api import Playwright

class MakeUp:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_url(self, url:str):
        self.page.goto(url)
        return(self)

    def test_Autorization(self):
        self.page.goto("https://makeup.com.ua/ua/")
        self.page.locator(".header-office").click()
        self.page.get_by_label("E-mail").click()
        self.page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
        self.page.get_by_label("E-mail").press("Tab")
        self.page.get_by_placeholder("Пароль").fill("13052000n")
        self.page.get_by_placeholder("Пароль").press("Enter")

    def test_checking_pages(self):
        self.page.get_by_role("link", name="Парфумерія", exact=True).click()
        self.page.goto("https://makeup.com.ua/ua/product/977/")
        self.page.get_by_title("В обране").click()
        self.page.locator("#popup__window").get_by_text("Не спостерігати за зміною ціни").click()
        self.page.get_by_role("link", name="2", exact=True).click()
        self.page.locator(".product__remove-button").first.click()
        self.page.get_by_text("Купити").nth(1).click()
        # Перевірка сторінки Оформлення замовлення
        self.page.get_by_text("Оформити замовлення").click()
        self.page.get_by_role("link", name="MAKEUP").click()

    def test_checking_others_pages(self):
        # Перевірка сторінки Доставка та оплата
        self.page.get_by_role("link", name="Доставка та Оплата").click()
        # Перевірка сторінки Про нас
        self.page.get_by_role("link", name="Про нас").click()
        self.page.goto("https://makeup.com.ua/ua/articles/")
        # Перевірка сторінки Акції
        self.page.get_by_role("link", name="Акції").click()
        # Перевірка сторінки Про магазин
        self.page.get_by_role("link", name="Про магазин").click()
        self.page.locator(".header-basket").click()
        self.page.locator(".header-office").click()
        self.page.get_by_role("link", name="Вихід").click()

    def test_product_search(self):
        self.page.goto("https://makeup.com.ua/ua/")
        # Перевірка кнопки пошуку товару
        self.page.locator(".search-button").first.click()
        # Перевірка пошуку товару
        self.page.get_by_placeholder("Понад 249 000 товарів").fill("крем для рук")
        self.page.get_by_placeholder("Понад 249 000 товарів").press("Enter")
        self.page.goto("https://makeup.com.ua/ua/product/32739/")

    def test_filter_check(self):
        self.page.goto("https://makeup.com.ua/ua/")
        # Перехід на сторінку Тіло і ванна
        self.page.get_by_role("link", name="Тіло і ванна").click()
        self.page.locator("#popularinput-checkbox-2243-29953").click()
        # Перехід на товар
        self.page.goto("https://makeup.com.ua/ua/categorys/321073/#o[2243][]=29953")

    def test_password_change_verification(self):
        self.page.goto("https://makeup.com.ua/ua/")
        self.page.locator(".header-office").click()
        self.page.get_by_text("Забули пароль?").click()
        self.page.wait_for_timeout(1500)
        self.page.get_by_role("textbox", name="E-mail").click()
        self.page.get_by_role("textbox", name="E-mail").fill("o.ionenko129@gmail.com")
        self.page.get_by_role("button", name="Нагадати").click()
        self.page.locator("#popup__window div").first.click()

    def test_email_change_verification(self):
        self.page.goto("https://makeup.com.ua/ua/")
        self.page.locator(".header-office").click()
        self.page.get_by_label("E-mail").fill("o.ionenko129@gmail.com")
        self.page.get_by_role("button", name="Увійти").click()

    def test_verification_without_login(self):
        self.page.goto("https://makeup.com.ua/ua/")
        self.page.locator(".header-office").click()
        self.page.get_by_placeholder("Пароль").click()
        self.page.get_by_placeholder("Пароль").fill("13052000n")
        self.page.get_by_role("button", name="Увійти").click()
    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

