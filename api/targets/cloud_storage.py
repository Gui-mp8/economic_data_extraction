import json
from typing import List, Dict, Any

from google.cloud import storage

class CloudStorage:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.storage = storage.Client(project=self.config["project_id"])
        self.bucket = self.storage.bucket(self.config["service"]["cloud_storage"]["bucket_name"])

    def upload_json(self, data: List[Dict[str, Any]], destination_blob_name: str) -> None:

        json_data = json.dumps(data, indent=4)

        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_string(json_data, content_type='application/json')

        print(f"Data successfully uploaded !")

