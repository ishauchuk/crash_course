def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile(
    'albert', 'enstein', location='princeton', field='physics'
    )
print(user_profile)