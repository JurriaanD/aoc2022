import re
import operator
import math

class ItemTranfer:
    def __init__(self, item, monkey_num):
        self.item = item
        self.monkey_num = monkey_num

    def __str__(self):
        return f"Tranfering {self.item} to monkey {self.monkey_num}"

class Monkey:
    def __init__(self):
        self.items_ = []
        self.operation = None
        self.successor = None
        self.inspection_count = 0

    def add_item(self, item: int):
        self.items_.append(item)

    def set_items(self, items):
        self.items_ = items

    def set_operation(self, operation):
        self.operation = operation

    def set_successor_func(self, successor):
        self.successor = successor

    def get_item_transfers(self, lcm):
        item_transfers = []
        for item in self.items_:
            new_item = self.operation(item) % lcm # // 3
            succ = self.successor(new_item)
            self.inspection_count += 1
            item_transfers.append(ItemTranfer(new_item, succ))
        self.items_ = []
        return item_transfers

    def __repr__(self):
        return str(self.items_)

def build_value_lambda(rhs_str):
    if rhs_str == "old":
        return lambda op: (lambda x: op(x, x))
    else:
        return lambda op: (lambda x: op(x, int(rhs_str)))

def build_op_lambda(opstr, value_lambda):
    if opstr == '+':
        return value_lambda(operator.add)
    elif opstr == '*':
        return value_lambda(operator.mul)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def createsucc(divby, iftrue, iffalse):
    return lambda item: iftrue if (item % divby == 0) else iffalse

with open("11.in") as f:
    # Parse the input
    monkeys = []
    lines = [x.strip() for x in f.readlines()]
    monkey_inputs = chunks(lines, 7)
    divbys = []

    for monkey_input in monkey_inputs:
        monkey = Monkey()
        #[Monkey n, items, op, test condition, iftrue, iffalse, newline]

        # Items
        items = [int(x) for x in monkey_input[1].split(": ")[1].split(", ")]
        monkey.set_items(items)

        #Op 
        opstr, rhsstr = re.search(r"= old ([+*]) (\w+)", monkey_input[2]).groups()
        op = build_op_lambda(opstr, build_value_lambda(rhsstr))
        monkey.set_operation(op)

        # Successor
        divby = int(monkey_input[3].split("by ")[1])
        divbys.append(divby)
        iftrue = int(monkey_input[4].split(" to monkey ")[1])
        iffalse = int(monkey_input[5].split(" to monkey ")[1])
        monkey.set_successor_func(createsucc(divby, iftrue, iffalse))

        monkeys.append(monkey)

    lcm = math.lcm(*divbys)
    print(lcm)

    #for round in range(20):
    for round in range(10000):
        if (round % 100 == 0):
            print(round)
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for item_transfer in monkey.get_item_transfers(lcm):
                monkeys[item_transfer.monkey_num].add_item(item_transfer.item)

    counts = sorted([m.inspection_count for m in monkeys], reverse=True)
    print(counts)
    print(operator.mul(*counts[:2]))