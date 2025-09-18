def whatFlavors(cost, money):
    seen = {}

    for i, price in enumerate(cost):
        complement = money - price

        if complement in seen:
            print(seen[complement] + 1, i + 1)
            return

        seen[price] = i



# seen을 역으로 enumerate를 돌려놓은 걸 중점적으로 공부