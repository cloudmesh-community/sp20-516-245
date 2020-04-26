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

tmp = [
    "list", 
    "images", 
    "flavors", 

    "start", 
    "ping", 
    "terminate", 
    "destroy",
    "delete", 
    "status", 
    "ip", 
    "ssh",
    "keys",
    "stop", 

]

functionality_benchmark = ['list', 'images', 'flavors', 'create', 'stop']
#'create' needs cms set cloud={} 

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
def test_function(provider, function, function_name, setup_function, validation_function):

    test_name = f"test_{function_name}"

    variables = Variables()
    VERBOSE(variables.dict())

    key = variables['key']



    setup_function()

    StopWatch.start(test_name) 
    try:
        data = function() #TODO allow inputs from kwargs too #stop, start need image name
        StopWatch.stop(test_name)
        
        valid = validation_function(data)
        results = StopWatch.__str__()

    except IndentationError as e:
        print(e)
        StopWatch.stop(test_name)
        valid = False
        results = e
    
    results = f"{provider.name} {valid} {results}"
    return results

def no_setup():
    return

def validate_result_exists(result):
    return result != None

def main():
    #validators = {"list": validate_list}

    user = Config()["cloudmesh.profile.user"]

    name_generator = Name()
    name_generator.set(f"benchmark-{user}-vm-" + "{counter}")
    #name_generator.incr()


    providers = get_providers()
    results = {}

    for provider in providers:
        provider_name = provider.cloudname()

        print(provider_name)

        os.system(f"cms set cloud={provider_name}")

        results[provider_name] = {}

        for f_name in functionality_benchmark:
            try:

                #validation = validators[f_name]
                validation = validate_result_exists
                
                #Gets the implementation tied to a specific provider as a wrapped function, so it can be invoked directly, without needing to pass a self object
                func = getattr(provider, f_name) 
                result = test_function(provider, func, f_name, no_setup, validation)

                results[provider.name][f_name] = result
            except IndentationError as e:
                print(e)

    print(results)
        
    with open('benchmark.txt', 'w') as f:
        print(results, file=f)

    #TODO process data and write to file
    # "{provider} {label} {start} {end} {elapsed} {status} {newline}"

if __name__ == '__main__':
    Benchmark.debug()
    #user = Config()["cloudmesh.profile.user"]

    main()