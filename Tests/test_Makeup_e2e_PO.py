def test_Makeup_e2e(desktop_makeup):
    desktop_makeup.open_url("https://makeup.com.ua/ua/")
    desktop_makeup.Autorization()
    desktop_makeup.checking_pages()
    desktop_makeup.checking_others_pages()

def test_Makeup_negative(desktop_makeup):
    desktop_makeup.product_search()

def test_Makeup_negative2(desktop_makeup):
    desktop_makeup.filter_check()

def test_Makeup_negative3(desktop_makeup):
    desktop_makeup.password_change_verification()

def test_Makeup_negative4(desktop_makeup):
    desktop_makeup.email_change_verification()

def test_Makeup_negative5(desktop_makeup):
    desktop_makeup.verification_without_login()
