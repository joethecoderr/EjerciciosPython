def run():
    even = [num for num in range(1,31) if num % 2 == 0]
    print(even)
    sqrs = {num: num**2 for num in range(1,11)}
    print(sqrs)

if __name__ == '__main__':
   
    run()