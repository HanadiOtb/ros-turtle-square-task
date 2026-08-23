#!/usr/bin/env python3
import queue
import time

def main():
    message_queue = queue.Queue()
    
    # Publisher
    custom_msg = "Smart Methods - Custom Message Sent Successfully!"
    message_queue.put(custom_msg)
    print(f"[Publisher]: {custom_msg}")
    
    time.sleep(0.5)
    
    # Subscriber
    received_msg = message_queue.get()
    print(f"[Subscriber]: {received_msg}")

if __name__ == '__main__':
    main()
