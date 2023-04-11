# 1. 아래 문자열의 길이를 구해보세요.

q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(f"1. q1의 길이 : {len(q1)}")


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print("2. apple;orange;banana;lemon")


# 3. 화면에 * 기호 100개를 표시하세요.

star = "*"
print(f"3. {star * 100}")


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

str = "30"
print(f"4. 정수형 : {int(str)}, 정수형 : {float(str)}, 복소수형 : {complex(str)}, 문자형 : {str}")


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

str = "Niceman"
target = "man"
index = str.index(target)
print(f"5. {str[index:index + len(target)]}")


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

str = "Strawberry"
print(f"6. {str[::-1]}")


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

str = "010-7777-9999"
print(f"7. {''.join(str.split('-'))}")


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

str = "http://daum.net".replace("http://", "")
print(f"8. {str}")


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

str = "NiceMan"
print(f"9. {str.upper()}, {str.lower()}")


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

str = "abcdefghijklmn"
print(f"10. {str[2:5]}")


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

list = ["Banana", "Apple", "Orange"]
list.remove("Apple")
print(f"11. {list}")


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

tup = (1, 2, 3, 4)
print(f"12. {[n for n in tup]}")


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dict = {
    "성인": 100000,
    "청소년": 70000,
    "아동": 30000
}
print(f"13. {dict}")


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dict["소아"] = 0
print(f"14. {dict}")


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print(f"15. {[key for key in dict.keys()]}")


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print(f"16. {[value for value in dict.values()]}")