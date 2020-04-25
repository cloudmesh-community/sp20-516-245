# fa19-516-000 E.Cloudmesh.Common.3
from cloudmesh.common.FlatDict import FlatDict

test_dict = {
    "username": "baker203",
    "classes": {
        "cloud_computing": "E516",
        "data_mining": "B565",
        "machine_learning": "B555"

    }
}

print(FlatDict(test_dict, sep="."))
