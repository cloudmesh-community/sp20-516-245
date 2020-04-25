# fa19-516-000 E.Cloudmesh.Common.2
from cloudmesh.common.dotdict import dotdict

test_dict = {
    "username": "baker203",
    "classes": {
        "cloud_computing": "E516",
        "data_mining": "B565",
        "machine_learning": "B555"

    }
}

x = dotdict(test_dict)
print(x)
print('print(x["username"])')
print(x["username"])
print('print(x.username)')
print(x.username)



