# circleci_stat: Python lib to fetch test statistics thru CircleCI RESTful WebAPI


![TravisCI](https://travis-ci.org/maxwu/circleci_stat.svg?branch=master)
![TravisCI](https://travis-ci.org/maxwu/circleci_stat.svg?branch=dev)

This Python lib is developed to support fetching build artifacts from circleci cloud. 
It also supports a fundamental statistic analysis to filter the high runners in UT.

The code followed some of the ideas in previous Bamboo RESTful experiences on XUnit fetching and counting.

Furthermore, a refactored lib will be generated to support all below services:
    
    - circleci (In progress); 
    - TravisCI;
    - Bamboo;
    - Jenkins;

- Feb 09, Add UT and removed casual codes/doctest/ut.
- Jan 20, The prototype with IPython Notebook finished.

