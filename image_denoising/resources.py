import os
import json


class Resources:
    def __init__(self, resource_dir: str):
        self._resource_dir = resource_dir

    def get_resource_path(self, resource: str):
        return os.path.join(self._resource_dir, resource)

    # def load_json(self, resource: str):
    #     with open(self.get_resource_path(resource)) as f:
    #         json_file = json.load(f)
    #     return json_file
