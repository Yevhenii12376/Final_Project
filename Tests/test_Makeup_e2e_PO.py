def test_Makeup_e2e(desktop_makeup):
    desktop_makeup.open_url("https://makeup.com.ua/ua/")
    desktop_makeup.test_Autorization()
    desktop_makeup.test_checking_pages()
    desktop_makeup.test_checking_others_pages()

def test_Makeup_negative(desktop_makeup):
    desktop_makeup.test_product_search()
    desktop_makeup.test_filter_check()
    desktop_makeup.test_password_change_verification()
    desktop_makeup.test_email_change_verification()
    desktop_makeup.test_verification_without_login()