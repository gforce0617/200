from itertools import product


def expr(p):
    return "{}9{}8{}7{}6{}5{}4{}3{}2{}1{}0".format(*p)


def gen_expr():
    op = ['+', '-', '']
    return [expr(p) for p in product(op, repeat=10) if p[0] != '+']


def all_exprs():
    values = {}
    for expr in gen_expr():
        val = eval(expr)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values


def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
        print(s)


sum_to(200)
