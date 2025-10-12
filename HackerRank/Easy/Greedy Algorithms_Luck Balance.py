def luckBalance(k, contests):
    important = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 0:
            total_luck += luck
        else:
            important.append(luck)

    important.sort(reverse=True)

    total_luck += sum(important[:k])      
    total_luck -= sum(important[k:])      

    return total_luck


# append로 새로 만들어서 reverse를 한다니 대단하다.
# :k, k:등 기억해둘 것.