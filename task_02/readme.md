# TASK 2
### 객체지향 (클래스설계2)

> 목표 : 인스턴스 생명주기를 선택하고 설계할 수 있다.


### [과제] 다음의 클래스를 총 세종류의 다른 클래스로 설계한다.

    Class MyClass {
        String myString = null;
    }

1. 여러번 생성이 가능하며, 각기 다른 값을 가질 수 있다. 값이 할당되기 전에는 인스턴스를 생성할 수 없다.
2. 오직 한 번만 생성되며, 생성 시 넘겨주는 값은 myString에 할당된다. 해당 값은  프로그램 종료시까지 전체 공유가 된다.
3. 오직 한 번만 생성되며, 생성 시 넘겨주는 값은 myString에 할당된다. 해당 값은  프로그램 종료시까지 전체 공유가 되며, 두 번 다시 변경할 수 없다.