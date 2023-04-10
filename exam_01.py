from utils import benchmark

DAN = range(2, 1000000)
SEQ = range(1, 10)

# 매 반복마다 print 함수 호출
@benchmark
def case_01():
    for i in DAN:
        for j in SEQ:
            print(f"{i} * {j} = {i * j}")

# list에 추가한 뒤 한번에 출력
@benchmark
def case_02():
    result = [f"{i} * {j} = {i * j}\n" for i in DAN for j in SEQ]
    print("".join(result))

# generator 사용
@benchmark
def case_03():
    result = (f"{i} * {j} = {i * j}\n" for i in DAN for j in SEQ)
    print("".join(result))

# case_01()
# case_02()
# case_03()