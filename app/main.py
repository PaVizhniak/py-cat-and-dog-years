def get_human_age(cat_age: int, dog_age: int) -> list:
    result = [0, 0]

    while cat_age >= 15:
        if cat_age >= 15:
            result[0] += 1
            cat_age -= 15

            if cat_age >= 9:
                result[0] += 1
                cat_age -= 9

                if cat_age >= 4:
                    total_cat_age = cat_age // 4
                    result[0] += total_cat_age
                    cat_age -= cat_age

    while dog_age >= 15:
        if dog_age >= 15:
            result[1] += 1
            dog_age -= 15

            if dog_age >= 9:
                result[1] += 1
                dog_age -= 9

                if dog_age >= 5:
                    total_dog_age = dog_age // 5
                    result[1] += total_dog_age
                    dog_age -= dog_age

    return result
