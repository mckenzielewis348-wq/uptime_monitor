import time
import urllib.request
import urllib.error

# List of URLs you want to monitor
TARGETS = [
    "https://github.com",
    "https://vercel.com",
    "https://google.com"
]

CHECK_INTERVAL = 5  # Seconds between checks (for testing)

def check_site(url):
    start_time = time.time()
    try:
        # Send a request with a user-agent header to avoid being blocked
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            end_time = time.time()
            response_time = round((end_time - start_time) * 1000, 2)
            
            if response.status == 200:
                print(f"🟢 [UP] {url} - Status: {response.status} - Time: {response_time}ms")
            else:
                print(f"🟡 [WARNING] {url} - Status: {response.status}")
                
    except urllib.error.URLError as e:
        print(f"🔴 [DOWN] {url} - Error: {e.reason}")

def main():
    print("🚀 Starting Uptime Monitor... Press Ctrl+C to stop.\n")
    try:
        while True:
            for site in TARGETS:
                check_site(site)
            print("-" * 40)
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n👋 Uptime Monitor stopped. Have a great day!")

if __name__ == "__main__":
    main()
