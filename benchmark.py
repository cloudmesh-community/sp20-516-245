import os

from pprint import pprint
from time import sleep

import pytest
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.compute.vm.Provider import Provider
from cloudmesh.configuration.Config import Config
from cloudmesh.management.configuration.name import Name
from cloudmesh.mongo.CmDatabase import CmDatabase

Benchmark.debug()

user = Config()["cloudmesh.profile.user"]
#variables = Variables()
#VERBOSE(variables.dict())

#key = variables['key']

#cloud = variables.parameter('cloud')

# print(f"Test run for {cloud}")


clouds = ["google", "azure"] # TODO get real list
#clouds = Provider.get_kind()
print(clouds)
providers = []
for cloud in clouds:
    try:
        p = Provider(name=cloud)
        providers.append(p) 
    except Exception as e:
        #print(e)
        #print("error getting cloud provider for : {}".format(cloud))
        continue
    
def test_list(provider):
    #Benchmark.Start()
    StopWatch.start("test_list") 
    data = provider.list()
    StopWatch.stop("test_list")
    results = StopWatch.__str__()
    results = f"{provider.name} {results}"
    return results

def test_flavors(provider):
    StopWatch.start("test_flavors") 
    data = provider.flavors()
    StopWatch.stop("test_flavors")
    results = StopWatch.__str__()
    results = f"{provider.name} {results}"
    return results

def test_images(provider):
    StopWatch.start("test_images") 
    data = provider.images()
    StopWatch.stop("test_images")
    results = StopWatch.__str__()
    results = f"{provider.name} {results}"
    return results

def test_create(provider):
    StopWatch.start("test_create") 
    data = provider.start()
    StopWatch.stop("test_create")
    results = StopWatch.__str__()
    results = f"{provider.name} {results}"
    return results

# Need to confirm command gives the proper output before returning timing result
# stop, start, boot, ping, terminate, delete, status, ip, ssh, 

#TODO process data and write to file
# "{label} {start} {end} {elapsed} {status} {newline}"
times = []
for p in providers:
    times.append(test_list(p))
    times.append(test_flavors(p))
    times.append(test_images(p))

print(times)
