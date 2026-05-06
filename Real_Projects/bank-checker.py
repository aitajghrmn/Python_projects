'''Task 🎯
Bank hesabı sistemi yaz.
Bir BankAccount class-ı olsun. İçində:

owner — hesab sahibinin adı
balance — balans (gizli olsun)

Qaydalar:

Balans mənfi ola bilməz
deposit() metodu ilə pul əlavə etmək olsun
withdraw() metodu ilə pul çıxarmaq olsun — amma balansdan çox çıxarmaq olmaz
Balansı getter ilə oxumaq olsun'''


class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance


    @property
    def balance(self):
      return self.__balance


    @balance.setter
    def balance(self,deger):
      if deger < 0 :
        print ("Balans menfi ola bilmez")

      else :
        self.__balance=deger

    def deposit(self,mebleg):
       self.__balance+=mebleg
       print(f"{mebleg} əlavə edildi. Balans: {self.__balance}")

    def withdraw (self,mebleg):
       if mebleg > self.__balance:
          print("Balansdan cox cixarmag olmaz")
       else:
          self.__balance-=mebleg
          print(f"{mebleg} balansinizdan cixarildi.Balans : {self.__balance}")

hesab = BankAccount("Aitaj", 100)
print(hesab.balance)   
hesab.deposit(50)      
hesab.withdraw(200)    
hesab.withdraw(80)     
print(hesab.balance)
