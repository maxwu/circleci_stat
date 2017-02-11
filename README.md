# circleci_stat: Python lib to fetch test statistics thru CircleCI RESTful WebAPI


master ![TravisCI](https://travis-ci.org/maxwu/circleci_stat.svg?branch=master) 
       [![codecov](https://codecov.io/gh/maxwu/circleci_stat/branch/master/graph/badge.svg)](https://codecov.io/gh/maxwu/circleci_stat)

dev    ![TravisCI](https://travis-ci.org/maxwu/circleci_stat.svg?branch=dev)
       [![codecov](https://codecov.io/gh/maxwu/circleci_stat/branch/dev/graph/badge.svg)](https://codecov.io/gh/maxwu/circleci_stat) 

[![CircleCI](https://circleci.com/gh/maxwu/circleci_stat.svg?style=svg)](https://circleci.com/gh/maxwu/circleci_stat)

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

----
Sample result format from circleci RESTful WebAPI.
- Checking recent 30 build summary

```json
{
  "vcs_revision" : "73b470133596aa77715290f613808647d9eda8b9",
  "vcs_tag" : null,
  "build_num" : 51,
  "infrastructure_fail" : false,
  "committer_email" : "maxwunj@gmail.com",
  "previous" : {
    "build_num" : 50,
    "status" : "canceled",
    "build_time_millis" : 592484
  },
  "status" : "timedout",
  "committer_name" : "maxwu",
  "retries" : null,
  "subject" : "Remove synch from DriverFactory",
  "vcs_type" : "github",
  "timedout" : true,
  "dont_build" : null,
  "lifecycle" : "finished",
  "no_dependency_cache" : true,
  "stop_time" : "2017-01-13T00:08:39.539Z",
  "ssh_disabled" : false,
  "build_time_millis" : 770258,
  "circle_yml" : {
    "string" : "machine:\n  java:\n    version: oraclejdk8\ntest:\n  post:\n    - mkdir -p $CIRCLE_TEST_REPORTS/junit/\n    - find . -type f -regex \".*/target/surefire-reports/.*xml\" -exec cp {} $CIRCLE_TEST_REPORTS/junit/ \\;\n"
  },
  "messages" : [ ],
  "is_first_green_build" : false,
  "job_name" : null,
  "start_time" : "2017-01-12T23:55:49.281Z",
  "canceler" : null,
  "all_commit_details" : [ {
    "committer_date" : "2017-01-13T12:35:16+13:00",
    "body" : "",
    "branch" : "dev",
    "author_date" : "2017-01-13T12:35:16+13:00",
    "committer_email" : "maxwunj@gmail.com",
    "commit" : "73b470133596aa77715290f613808647d9eda8b9",
    "committer_login" : "maxwu",
    "committer_name" : "maxwu",
    "subject" : "Remove synch from DriverFactory",
    "commit_url" : "https://github.com/maxwu/cucumber-java-toy/commit/73b470133596aa77715290f613808647d9eda8b9",
    "author_login" : "maxwu",
    "author_name" : "maxwu",
    "author_email" : "maxwunj@gmail.com"
  } ],
  "outcome" : "timedout",
  "vcs_url" : "https://github.com/maxwu/cucumber-java-toy",
  "author_name" : "maxwu",
  "node" : null,
  "queued_at" : "2017-01-12T23:55:49.258Z",
  "canceled" : false,
  "author_email" : "maxwunj@gmail.com"
}
```