def fib_num(number: int) -> int:

    if number < 0 :
        raise ValueError(
            "Number has be to non-negative"
        )
    elif number <= 1:
        return number
    else:
        return fib_num(number - 1) + fib_num(number - 2)
