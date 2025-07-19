def dictionary_operations(fruit_prices: dict, fruits: list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    order_print(fruit_prices)  # this function is in the hidden code

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2
    order_print(fruit_prices)

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2
    order_print(fruit_prices)

    # delete both key and value for fruits[3] from fruit_prices
    del fruit_prices[fruits[3]]
    order_print(fruit_prices)

    # print the price of fruits[4]

    print(fruit_prices.get(fruits[4]))

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(sorted(fruit_prices.keys()))

    # print the prices of the fruits as a list sorted in ascending order.
    print(sorted(fruit_prices.values()))


def increase_prices(fruit_prices: dict) -> None:
    """
    Increase the prices of every fruit by 20 percent and round to two decimal places

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    None - Do not return any thing - modify inplace
    """
    for f in fruit_prices:
        fruit_prices[f] = round(fruit_prices[f] * 1.20, 2)


def dict_from_string(string: str, key_type, value_type):
    """
    Given a string where each line has a comma seperated key-value pair, create a dictionary out of it. Also convert the types of key and values to the given types.

    Arguments:
    string - str: string to be parsed
    key_type - class: the data type of the keys
    value_type - class: the data type of the values

    Return:
    D - dict: the output dictionary
    """
    D = {
        key_type(k): value_type(v)
        for k, v in (line.split(",") for line in string.strip().splitlines())
    }
    return D


def dict_to_string(D: dict) -> str:
    """
    Convert the given dictionary back to the string fromat produced by `dict_from_string`. Again, do not use loops or conditionals, use comprehensions.

    """
    return "\n".join([f"{key},{value}" for key, value in D.items()])
