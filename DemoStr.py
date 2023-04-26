#DemoStr.py

#print(dir(str))

strA = "리안이 최고"
strB = "rian is Best Kid"
print(len(strA))
print(len(strB))
print(strB.capitalize()) #첫문자를 대문자로
print(strB.count("i"))
print(strB.startswith("ri"))
print(strB.endswith("id"))
print(strB.upper())
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())

data = "<<< spam and ham >>>"
result=data.strip("<> ")
print(data)
result =result.replace("spam","spam egg")
print(result)
lst=result.split()
print(lst)
print("--- 다시 하나의 문자열 ---")
print(":)".join(lst))
