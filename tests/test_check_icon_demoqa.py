from pages.demoqa import DemoQa


def test_icon_exists(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()

    # if icon is None:
    #   print("Элемент не найден")
    # else:
    #  print("Элемент найден")


