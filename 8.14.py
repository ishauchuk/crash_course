
def make_car(first, last, **car_info):
    car_info['first'] = first
    car_info['last'] = last
    return car_info

# car_new = make_car('subaru', 'outback', color='blue', tow_package=True)
car_new = make_car('subaru', 'outback', )
print(car_new)