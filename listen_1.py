import os
import threading

print(f"Используется процесс {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"В данный момент исполняется {total_threads} потоков")
print(f"Имя текущего потока {thread_name}")