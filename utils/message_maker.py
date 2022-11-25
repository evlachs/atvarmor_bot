from keyboards import see_more_keyboard_maker


def make_post_message(post: dict | list) -> dict:
    msg = {}
    s = ''
    if isinstance(post, dict):
        if post['img']:
            msg['img'] = post['img']
            post.pop('img')
        if post['permalink']:
            msg['keyboard'] = see_more_keyboard_maker(post['permalink'])
            post.pop('permalink')
        for content in post.values():
            s += f'{content}\n\n'
        msg['text'] = s
        return msg
    elif isinstance(post, list):
        for p in post:
            if p['img']:
                msg['img'] = p['img']
                p.pop('img')
            for content in p.values():
                s += f'{content}\n\n'
            s += '-'*10 + '\n\n'
        msg['text'] = s
        return msg

