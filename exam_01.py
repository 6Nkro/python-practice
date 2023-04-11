from utils import benchmark

DAN = range(2, 100000)
SEQ = range(1, 10)

# 매 반복마다 print 함수 호출
# case_01 함수 실행 시간: 2.8958 초
# case_01 함수 메모리 사용량: 0.0078 MiB
@benchmark
def case_01():
    for i in DAN:
        for j in SEQ:
            print(f"{i} * {j} = {i * j}")

# list에 추가한 뒤 한번에 출력
# case_02 함수 실행 시간: 0.5788 초
# case_02 함수 메모리 사용량: 1.9844 MiB
@benchmark
def case_02():
    result = [f"{i} * {j} = {i * j}\n" for i in DAN for j in SEQ]
    print("".join(result))

# generator 사용
# case_03 함수 실행 시간: 0.6699 초
# case_03 함수 메모리 사용량: 1.8633 MiB
@benchmark
def case_03():
    result = (f"{i} * {j} = {i * j}\n" for i in DAN for j in SEQ)
    print("".join(result))

# case_01()
# case_02()
# case_03()