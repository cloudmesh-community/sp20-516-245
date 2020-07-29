# Compute Benchmark Project 

This project focused on applying to multiple cloud providers, updating documentation of registration and usage, and providing benchmark data for all of those clouds. It provides an important comparison of the current functionality and relative speed of multiple different cloud providers. 


## Bug Fixes
When benchmarking the clouds, many of them worked okay, but some had significant issues that needed debugging that prevented the tests from being accurately run. 

- For Azure, there was a bug where a resource group needed to be created, and set in cloudmesh. There are a number of ways this can go wrong, but I see no way the process can be streamlined, so a working method was documented.  https://github.com/cloudmesh/cloudmesh-manual/pull/68/commits/5717c4b2d22471983bb40d5ec166a3439cde6a52

- Aws test updates https://github.com/cloudmesh/cloudmesh-cloud/pull/349

- Azure Covid documentation update https://github.com/cloudmesh/cloudmesh-manual/pull/71

- Another bug in Azure vm creation cenetered around tag length requirements. This pull request was made to fix a bug with Azure. It was fixed in parallel by Niranda, though he pushed changes after the pull request was made, so it was not accepted.  https://github.com/cloudmesh/cloudmesh-azure/pull/4

- Final benchmark csv https://github.com/cloudmesh/cloudmesh-cloud/pull/349

- General information was added about running the benchmark tests, and about specific issues that might be encountered in various clouds, for reasons that are hard to diagnose. https://github.com/cloudmesh/cloudmesh-cloud/blob/master/tests/cloud/README.rst


## Final Benchmark Results
The log files, provider csv files, and overall benchmark totals are provided here:  https://github.com/cloudmesh/cloudmesh-cloud/pull/349
