import sys


class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"[{self.product_id}] {self.name} - {self.price}₸ (қоймада: {self.stock})"

    def update_price(self, new_price: float):
        if new_price > 0:
            self.price = new_price
            return True
        return False

    def add_stock(self, amount: int):
        if amount > 0:
            self.stock += amount
            return True
        return False

    def remove_stock(self, amount: int):
        if 0 < amount <= self.stock:
            self.stock -= amount
            return True
        return False


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if product.product_id in self.products:
            print("Бұл ID бар, басқа ID енгізіңіз.")
        else:
            self.products[product.product_id] = product
            print(f"'{product.name}' дүкенге қосылды.")

    def list_products(self):
        if not self.products:
            print(" Дүкенде тауар жоқ.")
        else:
            print("\n=== Дүкендегі тауарлар ===")
            for p in self.products.values():
                print(p)

    def search_product(self, keyword: str):
        found = [p for p in self.products.values() if keyword.lower() in p.name.lower()]
        if not found:
            print("Іздеу нәтижесі табылмады.")
        else:
            print("\n Іздеу нәтижесі:")
            for p in found:
                print(p)

    def update_product_price(self, product_id: int, new_price: float):
        if product_id not in self.products:
            print(" Мұндай ID жоқ.")
            return
        product = self.products[product_id]
        if product.update_price(new_price):
            print(f"💰 '{product.name}' бағасы {new_price}₸ болып өзгертілді.")
        else:
            print(" Қате баға енгізілді.")

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            print(" Мұндай ID жоқ.")
            return
        deleted = self.products.pop(product_id)
        print(f"🗑️ '{deleted.name}' дүкеннен өшірілді.")

    def run(self):
        while True:
            print("\n=== Дүкен мәзірі ===")
            print("1. Тауарларды көру")
            print("2. Тауар қосу")
            print("3. Іздеу")
            print("4. Бағаны өзгерту")
            print("5. Тауарды жою")
            print("0. Шығу")

            choice = input(" Таңдау жасаңыз: ")

            if choice == "1":
                self.list_products()

            elif choice == "2":
                try:
                    pid = int(input("ID енгізіңіз: "))
                    name = input("Атауы: ")
                    price = float(input("Бағасы: "))
                    stock = int(input("Саны: "))
                    self.add_product(Product(pid, name, price, stock))
                except ValueError:
                    print(" Қате енгізу!")

            elif choice == "3":
                keyword = input("Іздеу сөзі: ")
                self.search_product(keyword)

            elif choice == "4":
                try:
                    pid = int(input("ID енгізіңіз: "))
                    new_price = float(input("Жаңа баға: "))
                    self.update_product_price(pid, new_price)
                except ValueError:
                    print(" Қате енгізу!")

            elif choice == "5":
                try:
                    pid = int(input("ID енгізіңіз: "))
                    self.delete_product(pid)
                except ValueError:
                    print(" Қате енгізу!")

            elif choice == "0":
                print("👋 Дүкен жабылды.")
                sys.exit()

            else:
                print(" Қате таңдау!")
                

if __name__ == "__main__":
    shop = Shop()
    # Бастапқы тауарлар
    shop.add_product(Product(1, "Нан", 150, 50))
    shop.add_product(Product(2, "Сүт", 300, 30))
    shop.add_product(Product(3, "Алма", 500, 20))
    shop.run()
