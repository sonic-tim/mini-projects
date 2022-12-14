def welcome_user():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    ambiguous = 'il1Lo0O'
    chars = ''    
    count = input(f'Какое количество паролей будем генерировать? \n')
    length = input(f'Укажите требуемую длину одного пароля от 8 символов - ')
    chars += (digits if input(f'Пароль должен содержать цифры? \nД - да, Н - нет\n').lower() in 'дl' else '')
    chars += (lowercase_letters if input(f'Пароль должен содержать прописные буквы? \nД - да, Н - нет\n').lower() in [
        'д', 'l'] else '')
    chars += (uppercase_letters if input(f'Пароль должен содержать строчные буквы? \nД - да, Н - нет\n').lower() in [
        'д', 'l'] else '')
    chars += (punctuation if input(f'Пароль должен содержать символы? \nД - да, Н - нет\n').lower() in 'дl' else '')
    symbols_ambiguous = (True if input(f'Пароль должен содержать неоднозначные символы "il1Lo0O"? \n\
    Д - да, Н - нет\n').lower() in 'дl' else False)
    if not symbols_ambiguous:
        for i in ambiguous:
            chars = chars.replace(i, '')
    generation_pass(int(count), int(length), chars)


def generation_pass(count, length, chars):
    from random import sample
    
    for i in range(1, count + 1):
        print(f'Пароль {i}: {"".join(sample(chars, length))}')


welcome_user()
