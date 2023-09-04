#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for round in range(x):
        n = nums[round]
        num_list = list(range(1, n + 1))
        turn = 0

        while len(num_list) > 0:
            if turn % 2 == 0:  # Maria's turn
                for num in num_list:
                    if is_prime(num):
                        num_list = [x for x in num_list if x % num != 0]
                        break
                else:
                    break
            else:  # Ben's turn
                for num in num_list:
                    if is_prime(num):
                        num_list = [x for x in num_list if x % num != 0]
                        break
                else:
                    break

            turn += 1

        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None


x = 3
nums = [4, 5, 1]

print(isWinner(x, nums))
