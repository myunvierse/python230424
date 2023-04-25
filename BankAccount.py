# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #인스턴스 멤버변수 (초기화)
        #클래스 내부에 변수명 숨김
        self.__id = id 
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance) # \ : 하나의 줄로 연결

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#account1.balance =15000000 #사고..? 안되
print(account1)
#print(account1.__balance) #privite 으로 클래스내에서 사용
print(account1._BankAccount__balance) # backdoor  같은
#실행파일로 만들면 또 숨길수 있다