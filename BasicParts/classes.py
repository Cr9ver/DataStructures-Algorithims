class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    


my_cookie1 = Cookie("green")
my_cookie2 = Cookie("blue")
cookie_one = my_cookie1.get_color()
cookie_two = my_cookie2.get_color()

print(f"Cookie one is {cookie_one}")
print(f"Cookie two is {cookie_two}")
