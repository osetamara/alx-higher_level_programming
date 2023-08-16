def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    weighted_average = total_score / total_weight
    return weighted_average