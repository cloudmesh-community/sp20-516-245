# Cloudmesh Compute Benchmark

This project focused on applying to multiple cloud providers, updating documentation of registration and usage, and providing benchmark data for all of those clouds. It provides an important comparison of the current functionality and relative speed of multiple different cloud providers. 


## Improvements

Some minor bug fixes needed to be applied (mostly done by others) so benchmarks could run more smoothly:

- For Azure, we needed to add resource groups There are a number of ways this can be done. A working method was documented [here](<https://github.com/cloudmesh/cloudmesh-manual/pull/68/commits/5717c4b2d22471983bb40d5ec166a3439cde6a52)

- Although a previous version of cludmesh worked, a student introduced a bug in the tag length. This was removed within one week by the student that introduced the bug.  

- Azure resource anavalability issue has been documented [here](https://github.com/cloudmesh/cloudmesh-manual/pull/71)

- Aws test were updated [here](<https://github.com/cloudmesh/cloudmesh-cloud/pull/349>)


## Final Benchmark Results

General information was added about running the benchmark tests, and about specific issues that might be encountered in [various clouds](https://github.com/cloudmesh/cloudmesh-cloud/blob/master/tests/cloud/README.rst).

The log files, provider csv files, and overall benchmark totals are provided 
[here](https://github.com/cloudmesh/cloudmesh-cloud/pull/349)
