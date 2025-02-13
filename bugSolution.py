def function(a, b):
    if b == 0:
        return 0  # Or raise an exception, return float('inf'), or handle as appropriate
    return a / b

result = function(10, 0) # Returns 0
result2 = function(10,2) # Returns 5.0