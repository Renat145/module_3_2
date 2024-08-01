def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if '@' not in recipient or not (recipient.endswith('.com') or recipient.endswith('.net') or recipient.endswith('.ru')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender or not (sender.endswith('.com') or sender.endswith('.net') or sender.endswith('.ru')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')



send_email('hello', 'renat@mail.net')