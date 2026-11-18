# LOG FILE ANALYZER USING PYTHON
# Sample server log data
logs = """
192.168.1.10 - - [18/Nov/2026] "GET /home HTTP/1.1" 200 1200
192.168.1.11 - - [18/Nov/2026] "GET /login HTTP/1.1" 200 800
192.168.1.10 - - [18/Nov/2026] "GET /home HTTP/1.1" 200 1200
192.168.1.12 - - [18/Nov/2026] "POST /login HTTP/1.1" 404 500
192.168.1.11 - - [18/Nov/2026] "GET /about HTTP/1.1" 200 900
192.168.1.10 - - [18/Nov/2026] "GET /contact HTTP/1.1" 500 300
192.168.1.12 - - [18/Nov/2026] "GET /home HTTP/1.1" 200 1200
invalid log line
"""
# Initialize dictionaries
ip_count = {}
endpoint_count = {}
error_count = {}

total_requests = 0
malformed_lines = 0

# Analyze each log line
for line in logs.strip().split("\n"):

    parts = line.split('"')

    if len(parts) < 3:
        malformed_lines += 1
        continue

    ip = line.split()[0]
    request = parts[1].split()
    status_part = parts[2].split()

    if len(request) < 2 or len(status_part) < 1:
        malformed_lines += 1
        continue

    endpoint = request[1]

    try:
        status = int(status_part[0])
    except ValueError:
        malformed_lines += 1
        continue

    total_requests += 1

    # Count IP addresses
    ip_count[ip] = ip_count.get(ip, 0) + 1

    # Count endpoints
    endpoint_count[endpoint] = endpoint_count.get(endpoint, 0) + 1

    # Count errors
    if status >= 400:
        error_count[status] = error_count.get(status, 0) + 1

# Display report
print("===== LOG FILE ANALYZER =====")

print("\nTotal Requests:", total_requests)

print("Total Error Responses:", sum(error_count.values()))

print("Malformed Lines:", malformed_lines)

print("\nError Status Counts:")
for status, count in error_count.items():
    print(status, ":", count)

print("\nIP Address Analysis:")
for ip, count in ip_count.items():
    print(ip, ":", count, "requests")

print("\nEndpoint Analysis:")
for endpoint, count in endpoint_count.items():
    print(endpoint, ":", count, "requests")

print("\n===== ANALYSIS COMPLETED =====")
