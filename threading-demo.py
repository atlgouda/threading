import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print('Sleeping {} second(s)...'.format(seconds))
    time.sleep(seconds)
    return 'Done Sleeping . . . {}'.format(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)



# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()


print ('Finished in {} second(s)'.format(round(finish-start, 2)))

# source: https://www.youtube.com/watch?v=IEEhzQoKtQU&list=WL&index=2