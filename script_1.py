from __future__ import annotations
import urwid


def check_password_length(password):
    password_length = len(password)
    if password_length > 12:
        return True
    return False


def find_any_digit(password):
    return any(letter.isdigit() for letter in password)


def find_any_letter(password):
    return any(letter.isalpha() for letter in password)


def find_any_upper_letter(password):
    return any(letter.isupper() for letter in password)


def find_any_lower_letter(password):
    return any(letter.islower() for letter in password)


def find_any_symbol(password):
    return any(not letter.isalnum() for letter in password)


def rate_password(password):
    password_checks = [
        check_password_length(password),
        find_any_digit(password),
        find_any_letter(password),
        find_any_upper_letter(password),
        find_any_lower_letter(password),
        find_any_symbol(password)
    ]
    password_rating = 0
    for password_check in password_checks:
        if password_check:
            password_rating += 2
    return password_rating


def on_ask_change(edit, new_edit_text):
    reply.set_text(f"Рейтинг пароля: {rate_password(new_edit_text)}")


ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')


def main():
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
