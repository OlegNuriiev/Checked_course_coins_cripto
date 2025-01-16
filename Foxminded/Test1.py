# a = "asger"
# b = 14
# c = a*b

# c: list = [2, 124, 'ewr', True]
# v: tuple = ('sdge', 123)
# d: set = {1, "213", 123}
# g: dict = {1: 1234, 2: "afwe"}
#
# if print(c.count(False)):
#     print('Complate')
# else:
#     c.append(False)
#     print(c.count(False))

# products = {"fastfood": "shaurma", "drink": "colla", "vegetables": "apples", "water": "water"}
#
# while products:
#     a = input("Введите продукт: ")
#     if a in products:
#         for i in products.values():
#             print(i)
#         products.pop(a)
#     else:
#         print("Нет продукта.")
#
# print("Все продукты закончились.")


# products = []
# while True:
#     stop = "stop"
#     a = input("Введите данные: ")
#     if a in products:
#         print("Это уже есть.")
#     elif a in stop:
#         break
#     else:
#         products.append(a)
#         with open("text.txt", "w", newline="") as file:
#             file.write(f"{products}\n")
#         print("Product found. The tags are in file tags.txt.")
