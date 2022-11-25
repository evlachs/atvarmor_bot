from keyboards import address_keyboard_maker


def make_address(post: dict) -> dict:
    msg = {}
    s = ''
    if post['yandex_link']:
        msg['keyboard'] = address_keyboard_maker(post['yandex_link'])
        post.pop('yandex_link')
    for content in post.values():
        s += f'{content}\n\n'
    msg['text'] = s
    return msg
