import math


class Pagination:

    def __init__(self, text, size_of_page):
        self.text = text
        if size_of_page > 0:
            self.size_of_page = size_of_page
        else:
            self.size_of_page = 5
        self.item_count = len(text)
        self.page_count = math.ceil(self.item_count / self.size_of_page)
        self.pages = list()
        page = ''
        for char in self.text:
            page += char
            if len(page) == self.size_of_page:
                self.pages.append(page)
                page = ''
        if len(page) != 0:
            self.pages.append(page)

    def count_items_on_page(self, number_of_page):
        try:
            if number_of_page > len(self.pages):
                raise BaseException
            return len(self.pages[number_of_page])
        except BaseException:
            print("Invalid index. Page is missing.")

    def display_page(self, number_of_page):
        try:
            if number_of_page > len(self.pages):
                raise BaseException
            return self.pages[number_of_page]
        except BaseException:
            print("Invalid index. Page is missing.")

    def find_page(self, text_to_find):
        try:
            occurences = list()
            number_of_page = 0
            if text_to_find in self.text:
                for page in self.pages:
                    if text_to_find.strip() in page or page.strip() in text_to_find:
                        occurences.append(number_of_page)
                    number_of_page += 1
                return occurences
            else:
                raise Exception
        except Exception:
            print(f"{text_to_find} is missing on the pages")


pages = Pagination('Your beautiful text', 5)

print(pages.page_count, pages.item_count, pages.pages)
print(pages.count_items_on_page(0))
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(7))
print(pages.display_page(0))
print(pages.find_page('Your'))
print(pages.find_page('e'))
print(pages.find_page('beautiful'))
print(pages.find_page('great'))
