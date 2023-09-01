import requests
import concurrent.futures
import time
import statistics

http_url = "http://localhost:8080/orders"
order_data = {
    "stoks": "CADUSD",
    "quantity": 10
}

ws_url = "ws://localhost:8080/ws"

http_timestamps = []

def send_post_request(url, data):
    """ Function to make post request and get start and end times"""
    try:
        start_time = time.time()  
        response = requests.post(url, json=data)
        end_time = time.time()  
        response.raise_for_status()  
        http_timestamps.append((start_time, end_time))  
        return response.json()  
    except Exception as e:
        return f"Error: {str(e)}"

# ThreadPoolExecutor with 100 worker threads for HTTP requests
num_http_requests = 100
with concurrent.futures.ThreadPoolExecutor(max_workers=num_http_requests) as http_executor:
    http_futures = [http_executor.submit(send_post_request, http_url, order_data) for _ in range(num_http_requests)]

concurrent.futures.wait(http_futures)

# Calculate average execution delay and standard deviation for HTTP requests
http_delays = [(b - a) for a, b in http_timestamps]
http_average_delay = round(sum(http_delays) / num_http_requests,3)
http_std_deviation = round(statistics.stdev(http_delays),3)

# Print out the results for HTTP requests
print(f"HTTP Average Execution Delay: {http_average_delay} seconds")
print(f"HTTP Standard Deviation: {http_std_deviation} seconds")


