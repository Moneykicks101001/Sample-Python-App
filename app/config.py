import os 
class Config: 
    APP_NAME = os.getenv("APP_NAME", "azure-demo-app") 
    ENVIRONMENT = os.getenv("ENVIRONMENT", "dev") 
    
    # Future Azure integrations 
    KEYVAULT_NAME = os.getenv("KEYVAULT_NAME", "") 
    STORAGE_ACCOUNT = os.getenv("STORAGE_ACCOUNT", "") 
    COSMOSDB_ENDPOINT = os.getenv("COSMOSDB_ENDPOINT", "")