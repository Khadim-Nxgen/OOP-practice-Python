# import csv
class Item():
  pass
#   Price_rate=0.8
#   all=[]
#
#   def __init__(self, name: str, price, quantitiy: float):
#     assert price >= 0, f"Price {price}is not greater than or equal to 0 "
#     assert quantitiy >= 0, f"quantitiy  {quantitiy}is not greater than or equal to 0 "
#     self._name=name
#     self.quantitiy=quantitiy
#     self.price=price
#
#     Item.all.append(self)
#   @property
#   def price(self):
#     return self.price
#
#   # def apply_increment(self,increment):
#   #   self.__price = self.__price + self.__price * increment
#   def discount_price(self):
#      self.price=self.price*self.Price_rate
#   @property
#   def name(self):
#     return self._name
#   @name.setter
#   def name(self, value):
#      self._name=value
#
#   def total_price(self):
#     return self.quantitiy*self.price
#
#
#   def __repr__(self):
#     return f"{self.__class__.__name__}({self.name},{self.quantitiy},{self.__price})"
#   @classmethod
#   def grab_from_cvs(cls):
#      with open("items.csv",'r') as f:
#        reader=csv.DictReader(f)
#        items=list(reader)
#      for item in items:
#       print(item)

  # @property
  # def read_only_name(self):
  #   return "AAA"



# Item.grab_from_cvs()
# print(Item.all)








# my_item.discount_price()
# print(my_item.price)
#
# my_item1=Item("laptop",5,1000)
# my_item1.Price_rate=0.7
# my_item1.discount_price()
# #
#
# print(my_item1.price)



# print(Item.all)
# for instance in Item.all:
#    print(instance.name,instance.quantitiy,instance.price)


def fun(x,y):
  return x+y

# if __name__=="__main__":
print("runt his code")





