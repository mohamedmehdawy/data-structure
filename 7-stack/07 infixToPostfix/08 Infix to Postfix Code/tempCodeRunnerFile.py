if __name__ == '__main__':
    print(InfixToPostfix('1+2+3'))	# 12+3+
    print(InfixToPostfix('1+2*3'))  # 123*+
    print(InfixToPostfix('2*3+4'))  # 23*4+
    print(InfixToPostfix('1+3*5-8/2'))  # 135*+82/-
    print(InfixToPostfix('2+3*4-5*6+7'))  # 234*+56*-7+