def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enque")
    
    queue = Queue()
    
    for ele in data:
        queue.enque(ele)

    
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  
