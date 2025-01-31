def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old!!"


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number>10:
        return "Greater"
    elif number<10:
        return "Lesser"
    else:
        return "Equal"


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(1, n+1):
        sum +=i
    return sum

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum_list = sum(numbers)
    max_list = max(numbers)
    min_list = min(numbers)
    return (sum_list, max_list, min_list)


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    output = []
    for name, score in students_dict.items():
        if score>80:
            output.append(name)
    return output

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    unique_list1 = set(list1)
    unique_list2 = set(list2)
    return unique_list1 & unique_list2

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    addition = a+b
    difference = a-b
    product = a*b
    if b == 0:
        quotient = "Undefined"  # Avoid division by zero
    else:
        quotient = a / b
    return {
        "sum": addition,
        "difference": difference,
        "product": product,
        "quotient": quotient
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    log_and = x and y
    log_or = x or y
    log_not_x = not x
    log_not_y = not y
    return {
        "and": log_and,
        "or": log_or,
        "not_x": log_not_x,
        "not_y": log_not_y
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b,
        "not_a": ~a,
        "not_b": ~b,
        "left_shift_a": a << 1,
        "left_shift_b": b << 1,
        "right_shift_a": a >> 1,
        "right_shift_b": b >> 1
    }