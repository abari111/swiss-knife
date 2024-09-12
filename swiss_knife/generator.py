import random
import string


def is_len_valid(passwd_ln) -> bool:
    if isinstance(passwd_ln, int) and passwd_ln > 12:
        return True
    else:
        return False


def passwd_generator(passwd_ln: int = 12) -> str:

    if not is_len_valid(passwd_ln):
        passwd_ln = 12

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    passwd = "".join(random.sample(characters, passwd_ln))

    return passwd


if __name__ == "__main__":
    passwd = passwd_generator()
    print(passwd)
