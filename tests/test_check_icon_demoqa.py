from pages.demoqa import DemoQa


def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.icon.click()
    assert demo_qa_page.exist_icon()


    # browser.get('http://demoqa.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print("элемент не найдет")
    # else:
    #     print("элемент найден")


