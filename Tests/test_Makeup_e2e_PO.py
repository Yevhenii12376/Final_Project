def test_Makeup_e2e(desktop_makeup):
    desktop_makeup.open_url("https://makeup.com.ua/ua/")
    desktop_makeup.test_Autorization()
    desktop_makeup.test_checking_pages()
    desktop_makeup.test_checking_others_pages()