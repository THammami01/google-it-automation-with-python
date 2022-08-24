#!/usr/bin/env python3

from multiprocessing import Pool

def run(task):
    print("Handling {}".format(task))

if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  p = Pool(len(tasks))
  p.map(run, tasks)
