import os
import inspect

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


def get_providers():
    clouds = ["google", "azure"] # Provider.get_kind()
    providers = []
    for cloud in clouds:
        try:
            p = Provider(name=cloud)
            providers.append(p) 
        except Exception as e:
            #print(e)
            #print("error getting cloud provider for : {}".format(cloud))
            continue
    return providers

#TODO take in function for ensuring command has proper result
def test_function(provider, function):
    test_name = f"test_{function.__name__}"

    StopWatch.start(test_name) 
    data = function() #TODO allow inputs from kwargs too
    StopWatch.stop(test_name)
    results = StopWatch.__str__()
    results = f"{provider.name} {results}"
    return results

def main():
    times = []
    function_names = ["list", "images", "flavors", "stop", "start", "boot", "ping", "terminate", "delete", "status", "ip", "ssh"]
    for provider in providers:
        for fname in function_names:
            func = getattr(p, fname)
            times.append(test_function(provider, func))

    #TODO process data and write to file
    # "{provider} {label} {start} {end} {elapsed} {status} {newline}"

if __name__ == '__main__':
    Benchmark.debug()
    #user = Config()["cloudmesh.profile.user"]

    main()