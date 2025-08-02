import os
import json
import requests
import datetime
import hashlib
import hmac
import base64

workspace_id = os.getenv("WORKSPACE_ID")
shared_key = os.getenv("SHARED_KEY")
log_type = "PipelineLogs"

# Load log file
with open("logs/pipeline_log.txt", "r") as file:
    log_content = file.read()

body = json.dumps({
    "TimeGenerated": datetime.datetime.utcnow().isoformat() + "Z",
    "LogContent": log_content
})

def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"{method}\n{content_length}\n{content_type}\n{x_headers}\n{resource}"
    bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = base64.b64encode(hmac.new(decoded_key, bytes_to_hash, hashlib.sha256).digest()).decode()
    return f"SharedKey {customer_id}:{encoded_hash}"

def post_data(customer_id, shared_key, body, log_type):
    method = "POST"
    content_type = "application/json"
    resource = "/api/logs"
    rfc1123date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    content_length = len(body)
    signature = build_signature(customer_id, shared_key, rfc1123date, content_length, method, content_type, resource)
    uri = f"https://{customer_id}.ods.opinsights.azure.com{resource}?api-version=2016-04-01"
    
    headers = {
        "Content-Type": content_type,
        "Authorization": signature,
        "Log-Type": log_type,
        "x-ms-date": rfc1123date
    }
    response = requests.post(uri, data=body, headers=headers)
    if 200 <= response.status_code <= 299:
        print("Logs sent to Azure Log Analytics successfully.")
    else:
        print(f"Error sending logs: {response.status_code}, {response.text}")

post_data(workspace_id, shared_key, body, log_type)
