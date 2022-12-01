def sequential_map(*args):
    container = args[-1]
    functions = args[:-1]
    for fun in functions:
        answer = list(map(fun, container))
    return answer

def consensus_filter(*args):
    container = args[-1]
    functions = args[:-1]
    for fun in functions:
        container = list(filter(fun, container))
    return container

def conditional_reduce(function1, function2, container):
    reduced_container = list(filter(function1, container))
    answer = reduced_container[0]
    for num in reduced_container[1:]:
        answer = function2(answer, num)
    return answer


def func_chain(*args):
    def inside_func(x):
        print(args)
        for function in list(args):
            x = function(x)
        return x
    return inside_func