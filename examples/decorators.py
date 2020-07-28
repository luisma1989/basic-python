PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Write your password:')

        if password == PASSWORD:
            return func()
        else:
            print('The password is incorrect.')

    return wrapper


@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return 'hola, {}'.format(name)


if __name__ == '__main__':
    # needs_password()
    print(say_my_name('Luisma'))
