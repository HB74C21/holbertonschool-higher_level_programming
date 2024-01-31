def add_tuple(tuple_a=(), tuple_b=()):
    first_t = tuple_a + (0, 0)
    second_t = tuple_b + (0, 0)

    result_t = (first_t[0] + second_t[0], first_t[1] + second_t[1])

    return result_t
