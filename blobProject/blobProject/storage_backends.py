# storage_backends.py

from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'blobexercisedjango'
    account_key = 'cZWg29+5/MFsynWCSf3V1uhFA+EQznGvWXcMAxIgbbaw2AlEO+6ng+lXoQZNr/UEefSs41Zgi4aZ+ASty6RbIA=='
    azure_container = 'pics'
    expiration_secs = None
