import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(" ")

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard1 = types.KeyboardButton(text="Lenovo")
    keyboard2 = types.KeyboardButton(text="Acer")
    keyboard3 = types.KeyboardButton(text="Asus")
    keyboard4 = types.KeyboardButton(text="Avtech")
    keyboard5 = types.KeyboardButton(text="HP")
    keyboard6 = types.KeyboardButton(text="TOSHIBA")
    keyboard7 = types.KeyboardButton(text="DELL")
    keyboard8 = types.KeyboardButton(text="Huawei")
    keyboard9 = types.KeyboardButton(text="brand unknown")
    keyboard10 = types.KeyboardButton(text="RAZER")
    keyboard11 = types.KeyboardButton(text="PRESTIGIO")
    keyboard12 = types.KeyboardButton(text="PRESTIGIO")
    keyboard13 = types.KeyboardButton(text="MSi")
    keyboard14 = types.KeyboardButton(text="Apple")
    markup.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9,
               keyboard10, keyboard11, keyboard12, keyboard13, keyboard14)
    bot.send_message(chat_id, f"Привет {first_name} !\n "
                   "Выбери марку ноутбука", reply_markup= markup)


@bot.message_handler(content_types=["text"])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == "Apple":
            link = "https://www.mediapark.uz"
            url = "https://www.mediapark.uz/products/category/218"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            section = soup.find_all("div", class_="goods-section-right-blocks")
            for products in section:
                product = products.find_all("div", class_="car-block")
                for item in product:
                    product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                    product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                    product_link = link + item.find("a", class_="product_list_img").get("href")
                    all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                    bot.send_message(chat_id, all_products)

    if message.text == "Lenovo":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=19&price_min=0&price_max=33880000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "Acer":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=21&price_min=2268000&price_max=13958000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "Asus":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=22&price_min=2270000&price_max=13960000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "Avtech":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=23&price_min=2271000&price_max=13961000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "HP":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=24&price_min=2270000&price_max=4890000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "TOSHIBA":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=24&price_min=2270000&price_max=4890000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "DELL":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=42&price_min=3800000&price_max=14250000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "Huawei":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=55&price_min=3799000&price_max=14249000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "brand unknown":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=81&price_min=8299000&price_max=9599000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "RAZER":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=121&price_min=8304000&price_max=9604000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "PRESTIGIO":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=163"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "CANYON":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=166&price_min=1033000&price_max=3883000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)

    if message.text == "MSI":
        link = "https://www.mediapark.uz"
        url = "https://www.mediapark.uz/products/category/22?brand%5B%5D=173&price_min=630000&price_max=15870000"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find_all("div", class_="goods-section-right-blocks")
        for products in section:
            product = products.find_all("div", class_="car-block")
            for item in product:
                product_name = item.find("span", class_="car-block-titile").get_text(strip=True)
                product_price = item.find("div", class_="price hvr-back-pulse").get_text(strip=True)
                product_link = link + item.find("a", class_="product_list_img").get("href")
                all_products = f"{product_name}\nЦена : {product_price}\nСcылка : {product_link}"
                bot.send_message(chat_id, all_products)


bot.polling(none_stop=True)
