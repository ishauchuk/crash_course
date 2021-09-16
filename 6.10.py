favorite_number = {
                    'Den': [6, 9, 11],
                    'Alex': [69, 911, 14], 
                    'John': [7, 19, 48], 
                    'Serg': [1, 1488, 21],
                    }


for key, value in favorite_number.items():
        print(f"{key}'s favorite numbers are:")
        for elem in value:
            print(f"\t{elem}")
