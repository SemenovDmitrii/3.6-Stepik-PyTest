import time
from selenium.webdriver.common.by import By

# Словарь
lan = {
    "ar": "أضف الى سلة التسوق",
    "ca": "Afegeix a la cistella",
    "cs": "Vložit do košíku",
    "da": "Læg i kurv",
    "de": "In Warenkorb legen",
    "en-gb": "Add to basket",
    "el": "Προσθήκη στο καλάθι",
    "es": "Añadir al carrito",
    "fi": "Lisää koriin",
    "fr": "Ajouter au panier",
    "it": "Aggiungi al carrello",
    "ko": "장바구니 담기",
    "nl": "Voeg aan winkelmand toe",
    "pl": "Dodaj do koszyka",
    "pt": "Adicionar ao carrinho",
    "pt-br": "Adicionar à cesta",
    "ro": "Adauga in cos",
    "ru": "Добавить в корзину",
    "sk": "Pridať do košíka",
    "uk": "Додати в кошик",
    "zh-cn": "Add to basket",
}


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_add = browser.find_element(By.CLASS_NAME,"btn-add-to-basket")
    assert button_add, "button is not"
    button_name = button_add.text
    lang = browser.execute_script(
        "return window.navigator.userLanguage || window.navigator.language"
    )
    lang_button_name = lan.get(lang)
    assert button_name == lang_button_name, "button is not"
