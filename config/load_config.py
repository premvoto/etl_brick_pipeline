from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import json

def load_config_from_key_vault():
    vault_url = "https://premkeyvlt.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    try:
        secret_value = client.get_secret("run-config").value
        return json.loads(secret_value)
    except Exception as e:
        print("Error retrieving config:", e)
        return None
