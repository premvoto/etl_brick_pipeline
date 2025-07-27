import os
import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

vault_url = "https://premkeyvlt.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

try:
    config = json.loads(client.get_secret("run-config").value)

    os.makedirs("/home/runner/.databricks", exist_ok=True)
    with open("/home/runner/.databricks/config", "w") as f:
        f.write(f"[DEFAULT]\n")
        f.write(f"host = {config['databricks_host']}\n")
        f.write(f"token = {config['databricks_token']}\n")

    print("Databricks CLI configured successfully.")
except Exception as e:
    print("Failed to configure Databricks CLI:", e)
    exit(1)
