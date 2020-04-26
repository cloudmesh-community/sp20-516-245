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

class ComputeBenchmark(object):

    def __init__(self, provider_name, function_name, setup_function=None, validation=None):
        try:
            self.provider_name = provider_name
            self.function_name = function_name

            self.test_name = f"test_{provider_name}_{function_name}"

            self.provider = Provider(name=provider_name)
            #Gets the implementation tied to a specific provider as a wrapped function, so it can be invoked directly, without needing to pass a self object\
            self.function = getattr(self.provider, function_name) 

            self._sf = setup_function if setup_function else self.no_setup
            self._vf = validation if validation else self.validate_result_exists

            self.result = ''
            self.status = False

        except Exception as e:
            print(e)
            self.result = f"{provider_name} {function_name} {False}"

    def no_setup(self):
        return

    def validate_result_exists(self, result):
        return result != None

    def setup_function(self):
        return self._sf()

    def validation_function(self, data):
        return self._vf(data)

# "{provider} {label} {start} {end} {elapsed} {status} {newline}"
class ComputeBenchmarkOutput(object):
    def __init__(self, provider, function, start, end, status, excpection=None):
        self.provider = provider
        self.function = function
        self.start = start
        self.end = end
        self.status = status
        self.exception = excpection
        self.duration = int(float(end) - float(start))

    def __str__(self):
        return f"{self.provider} {self.function} {self.start} {self.end} {self.duration} {self.status} {self.exception}"

    def __repr__(self):
        return f"{self.provider} {self.function} {self.start} {self.end} {self.duration} {self.status} {self.exception}"

functionality_benchmark = [
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

providers = Provider.get_kind() 

def test_function(benchmark_obj):

    os.system(f"cms set cloud={benchmark_obj.provider_name}")
    thrown = None

    benchmark_obj.setup_function()

    StopWatch.start(benchmark_obj.test_name) 
    try:
        data = benchmark_obj.function() #TODO allow inputs from args/kwargs too #e.g. stop, start need image name
        StopWatch.stop(benchmark_obj.test_name)
        
        valid = benchmark_obj.validation_function(data)
        results = StopWatch.__str__()

    except Exception as e:
        print(e)
        StopWatch.stop(benchmark_obj.test_name)
        valid = False
        thrown = e

    sw = StopWatch.__str__().split(" ")

    result = ComputeBenchmarkOutput(
        benchmark_obj.provider_name, 
        benchmark_obj.function_name,
        sw[1],
        sw[2],
        valid,
        thrown if thrown else None
    )
    
    return result

def main():
    Benchmark.debug()
    user = Config()["cloudmesh.profile.user"]

    name_generator = Name()
    name_generator.set(f"benchmark-{user}-vm-" + "{counter}")
    name_generator.incr()

    results = {}

    for provider in providers:
        results[provider] = {}

        for f_name in functionality_benchmark:
            results[provider][f_name] = []

            x = ComputeBenchmark(provider, f_name)

            try:
                results[provider][f_name].append(test_function(x))

            except Exception as e:
                print(e)

    #TODO use Tabulate writer to print
    print(results)
        
    with open('benchmark.txt', 'w'  ) as f:
        for provider, functions in results.items():
            for function in functions.keys():
                for result in functions[function]:
                    f.write(f"{result.__str__()}\n")

if __name__ == '__main__':
    main()