# fa19-516-000 E.Cloudmesh.Common.4
from cloudmesh.common.Shell import Shell as sh

result = sh.execute("pwd")
print(result)

result = sh.execute("grep", ['"introspection"', "e-cloudmesh-4.py"]) #Is this introspection!?
print(result)
