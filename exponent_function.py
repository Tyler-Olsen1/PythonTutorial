print(2**3)

# base_num = input("What's the base number")
# pow_num = input("Raise to which power?")
#

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))
