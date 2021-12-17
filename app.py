def check_prime(number):
    is_prime = None
    lily = []
    checkers = range(2, number)
    for i in checkers:
        if number % i == 0:
            lily.append(False)
        else:
            lily.append(True)

    if False in lily:
        is_prime = False
    else:
        is_prime = True
    return is_prime


print(check_prime(1729))
