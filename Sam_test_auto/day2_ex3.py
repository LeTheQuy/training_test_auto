# Verify the complexity of password
def verify_password(password):
    conditions_met = 0
    conditions_total = 6
    if len(password) in range(6, 16):
        conditions_met += 2
    else:
        conditions_met = 0
        print("password length must be between 6 and 16")

    # include Uppercase letter
    if password.lower() != password:
        conditions_met += 1
    else:
        print("password must have at least 1 uppercase letter")

    # include Lowercase letter
    if password.upper() != password:
        conditions_met += 1
    else:
        print("password must have at least 1 lowercase letter")

    # include digit(s)
    if len([x for x in password if x.isdigit()]) > 0:
        conditions_met += 1
    else:
        print("password must have at least 1 number between [0-9]")

    # include special symbols
    if len([char for char in password if char in ["$", "#", "@"]]) > 0:
        conditions_met += 1
    else:
        print("password must have at least 1 character from [$#@].")

    # # include special symbols
    # for char in password:
    #     if char in ["$", "#", "@"]:
    #         conditions_met += 1
    #         break
    # else:
    #     print("special character condition is not met")

    is_strong = False
    if conditions_met == conditions_total:
        is_strong = True

    return is_strong


if __name__ == "__main__":
    pass_word = input("enter a password: ")
    is_strong_pass = verify_password(pass_word)
    if is_strong_pass:
        print("strong password")
    else:
        print("not strong password")
