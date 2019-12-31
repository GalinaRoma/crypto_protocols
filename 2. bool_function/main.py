import random

analysts_count = 7


class Cryptanalyst:
    def __init__(self, n):
        self.n = n
        self.left_result = None
        self.right_result = None
        self.did_pay_for_dinner = False

    def throw_coins(self):
        rand = random.randint(0, 1)

        self.right_result = rand
        analysts[(self.n + 1) % analysts_count].left_result = rand


analysts = [Cryptanalyst(i) for i in range(0, analysts_count)]


def main():
    org_pay = random.randint(0, 1)
    if not org_pay:
        rand_analyst = random.randint(0, 2)
        analysts[rand_analyst].did_pay_for_dinner = True

    for i in range(0, analysts_count):
        analysts[i].throw_coins()

    for i in range(0, analysts_count):
        print('Человек ' + str(i + 1))
        print('Результат с левым соседом: ' + str(analysts[i].left_result))
        print('Результат с правым соседом: ' + str(analysts[i].right_result))
        print('Платит: ' + str(analysts[i].did_pay_for_dinner))
        print()

    who_pay()


def who_pay():
    result = 0

    for i in range(0, analysts_count):
        result += int((analysts[i].left_result != analysts[i].right_result) != analysts[i].did_pay_for_dinner)

    if not result % 2:
        print("Заплатила организация")
    else:
        print("Заплатил какой-то криптограф")


if __name__ == '__main__':
    main()
