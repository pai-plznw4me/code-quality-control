class Calculator:
    """
    Description:
     이항 연산을 하기 위한 계산기 코드 입니다.
     연산자를 선택해 어떤 연산을 수행 할지 결정 할 수 있습니다.
     현재 버전에서 연산자는 아래와 같이 2가지가 가능합니다. +, -

    Usage:
        # 더하기 연산
        calc = Calculator('+')
        calc(3, 5)

        # 빼기 연산
        calc = Calculator('-')
        calc(3,5)

    Args:
       operator: char

    """

    def __init__(self, operator):
        self.operator = operator

    def __call__(self, a, b):
        """
        Description:
            지정된 연사자를 활용해 이항 연산을 수행 합니다.

        :param float a: 이항 연산자 중 첫번째 인자
        :param float b: 이항 연산자 중 두번째 인자
        :return float: 이항 연사자 출력 값
        """
        if self.operator == '+':
            return a + b

        elif self.operator == '-':
            return a - b

        else:
            raise NotImplementedError


if __name__ == '__main__':
    calc = Calculator('+')
    print(calc(3, 4))
    calc = Calculator('-')
    print(calc(3, 4))
