import math
"""
길이를 설정해주기 위한 클래스 Line과 정사각형, 원, 정삼각형의 넓이를 반환하는 함수들을 포함한 figure.py
"""
class Line:
    """
    Length를 받아주고 수정해주는 클래스 Line
    """
    __length = 1
    def __init__(self, Length):
        """
        생성될 때 초기의 상태를 지정해준다. 만약 int, float 타입이 아니거나 입력받는 값이 0이하일 때 기본 값인 1로 설정된다.
        Args:
            Length: __length에 넣어줄 값
        Returns:
            아무 값도 리턴하지 않음
        """
        if (type(Length) == int or type(Length) == float) and Length > 0:
            self.__length = Length
        else:
            pass
        
    def get_length(self):
        """
        호출될 때 __length에 있는 값을 반환해 준다.
        Returns:
            self.__length
        """
        return self.__length
    
    def set_length(self, Length):
        """
        호출될 때 __length에 있는 값을 바꿔준다. 만약 int, float 타입이 아니거나 입력받는 값이 0이하일 때 이전 값이 유지된다.
        Args:
            Length: __length에 넣어줄 값
        Returns:
            아무 값도 리턴하지 않음
        Examples:
            >>> set_length(10) # __length의 값을 10으로 바꿔준다.
        """
        if (type(Length) == int or type(Length) == float) and Length > 0:
            self.__length = Length
        else:
            pass
        
        
def area_square(length):
    """
    매개변수 타입이 Line 클래스인 경우 Line 클래스에 있는 값 __length을 가져와서 제곱한 값을 반환하여 준다.
    Args:
        length : <class 'figure.Line'>
    Returns:
        n*n
    """
    if str(type(length))!= "<class 'figure.Line'>" :
        return 0
    else:
        n = length.get_length()
        return n*n
    
def area_circle(length):
    """
    매개변수 타입이 Line 클래스인 경우 Line 클래스에 있는 값 __length을 가져와서 제곱한 값에 PI를 곱하여 반환하여 준다.
    Args:
        length : <class 'figure.Line'>
    Returns:
        (n**2)*math.pi
    """
    if str(type(length))!= "<class 'figure.Line'>" :
        return 0
    else:
        n = length.get_length()    
        return (n**2)*math.pi

def area_regular_triangle(length):
    """
    매개변수 타입이 Line 클래스인 경우 Line 클래스에 있는 값 __length을 가져와서 제곱한 값에 (루트3)/4를 곱하여 반환하여 준다.
    Args:
        length : <class 'figure.Line'>
    Returns:
        (n**2)*math.sqrt(3)/4
    """
    if str(type(length))!= "<class 'figure.Line'>" :
        return 0
    else:
        n = length.get_length()
        return (n**2)*math.sqrt(3)/4