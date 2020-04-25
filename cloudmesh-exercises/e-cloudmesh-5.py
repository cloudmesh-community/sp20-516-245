# fa19-516-000 E.Cloudmesh.Common.5

from cloudmesh.common.StopWatch import StopWatch 
import time

StopWatch.start("outer")
time.sleep(1)
StopWatch.start("inner")
time.sleep(1)
StopWatch.stop("inner")
StopWatch.stop("outer")

print("Outer: {}".format(StopWatch.get("outer")))
print("Inner: {}".format(StopWatch.get("inner")))
print("Typo: {}".format(StopWatch.get("Inner")))
