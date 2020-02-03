def listDivide(numbers,divide=2):
    # defines the Count variable and sets it to 0
    Count = 0
    for number in numbers:
        if number % divide == 0:
            #Increments by 1
            Count = Count + 1

    return Count

class ListDivideException\
            (Exception):
    pass


def testListDivide():
    try:
        #  If the condition is true, it does nothing and your program just continues to execute.
        #  But if the assert condition evaluates to false, it raises an AssertionError error
        assert listDivide([1, 2, 3, 4, 5]) == 2
        assert listDivide([2, 4, 6, 8, 10]) == 5
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1, 2, 3, 4, 5], 1) == 5

    except Exception:
        raise ListDivideException()


testListDivide()

