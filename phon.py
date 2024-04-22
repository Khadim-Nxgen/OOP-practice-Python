from item import Item


class Phone(Item):

    # all=[]

    def __init__(self, name:str, quantitiy:float, __price, broken_phone=0):
        #calling super function from parent class
        super().__init__(
            name, quantitiy, __price
        )


        assert broken_phone >= 0, f"broken_phone   {broken_phone}is not greater than or equal to 0 "
        self.broken_phone=broken_phone

        # Phone.all.append(self)



My_phone=Phone("Motorola",20,300,3)
My_phone1=Phone("Motorola",20,30,20)

print(My_phone.total_price())

print(Item.all)
print(Phone.all)

