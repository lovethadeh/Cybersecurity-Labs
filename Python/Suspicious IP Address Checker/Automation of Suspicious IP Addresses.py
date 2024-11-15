import re
import requests
import csv
from datetime import datetime

# API configuration (replace with your actual API key)
# We can also Virus Total by replacing IPDB's Url and API key with Virus Total's
ABUSEIPDB_API_KEY = "your_api_key_here"
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"

# Function to extract IP addresses from logs
def extract_ips_from_logs(log_file):
    with open(log_file, "r") as f:
        logs = f.read()
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', logs)

# Function to check IP reputation via AbuseIPDB
def check_ip_reputation(ip):
    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    response = requests.get(ABUSEIPDB_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to analyze and generate a report
def analyze_ips_and_generate_report(log_file, output_file):
    unique_ips = set(extract_ips_from_logs(log_file))
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP Address", "Abuse Confidence Score", "Last Reported", "Country", "ISP", "Comment"])
        
        for ip in unique_ips:
            result = check_ip_reputation(ip)
            if result:
                data = result.get("data", {})
                writer.writerow([
                    ip,
                    data.get("abuseConfidenceScore", "N/A"),
                    data.get("lastReportedAt", "N/A"),
                    data.get("countryName", "N/A"),
                    data.get("isp", "N/A"),
                    data.get("domain", "N/A")
                ])

    print(f"Analysis complete. Report saved to {output_file}")

# Main process
if __name__ == "__main__":
    log_file = "server_logs.txt"  # Replace with the actual log file path
    output_file = f"suspicious_ips_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    analyze_ips_and_generate_report(log_file, output_file)
