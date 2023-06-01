import time

def count_to_n(n):
    start_time = time.time()
    for i in range(1, n+1):
        print(i)
    end_time = time.time()
    duration = end_time - start_time
    print(f'Time taken: {duration} seconds')

num = int(input('Enter a number: '))
estimated_time = num / 10
print(f'Estimated time: {estimated_time} seconds')
count_to_n(num)
