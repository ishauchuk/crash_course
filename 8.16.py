# import test

# user_profile = test.build_profile(
#     'albert', 'enstein', location='princeton', field='physics'
#     )
# print(user_profile)

# from test import build_profile
# user_profile = build_profile(
#     'albert', 'enstein', location='princeton', field='physics'
#     )
# print(user_profile)

# from test import build_profile as bp
# user_profile = bp(
#     'albert', 'enstein', location='princeton', field='physics'
#     )
# print(user_profile)

# import test as bp
# user_profile = bp.build_profile(
#     'albert', 'enstein', location='princeton', field='physics'
#     )
# print(user_profile)

from test import *
user_profile = build_profile(
    'albert', 'enstein', location='princeton', field='physics'
    )
print(user_profile)