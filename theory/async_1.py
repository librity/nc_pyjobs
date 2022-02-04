# python3 theory/async_1.py
# SOURCE: https://www.educba.com/python-async/

import queue


def task(name, sample_queue):
  if sample_queue.empty():
    print(f'Task {name} has nothing to do')
  else:
    while not sample_queue.empty():
      cnt = sample_queue.get()
      total = 0
      for x in range(cnt):
        print(f'Task {name} is running now')
        total += 1
        print(f'Task {name} is running with a total of: {total}')


def sample_async():
  sample_queue = queue.Queue()

  for work in [2, 5, 10, 15, 20]:
    sample_queue.put(work)
    tasks = [
        (task, 'Async1', sample_queue),
        (task, 'Async2', sample_queue),
        (task, 'Async3', sample_queue)
    ]

    for t, n, q in tasks:
      t(n, q)


if __name__ == '__main__':
  sample_async()
