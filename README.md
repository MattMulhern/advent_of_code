# pp_sensu_go
A simple python library for communicating with sensu go.

## Installation 
```
python setup.py install
```

### update_cluster_configs.py
This is intended to mainly run as an AWS lambda, but it can be called from commandline also.
#### AWS lambda

First, build the lambda .zip:
```
python setup.py ldist
```
Then upload dist/___.zip to your existing AWS lambda function. You will also need to set the entrypoint to `pp_sensu_reap_clients.lambda_entrypoint`.

Configuration options (given below) can all be specified by adding ENV_VARS as described in the usage below.
The only exception to this is that **the sensu password is obtained from AWS Secret Store only**

### Commandline
```
pp_sensu_reap_clients:1.2.0
usage: sensu_client_reaper [-h] [-l LOG_LEVEL] [-s SENSU_URL] [-S SENSU_PASS]
                           [--sensu-user SENSU_USER] [-c CMDB_URL]
                           [-C CMDB_PASS] [--cmdb-user CMDB_USER]
                           [-b BATCH_REQUESTS] [-t TIMEOUT] [-n DRY_RUN]
                           [--verify-ssl VERIFY_SSL]

Delete dead clients from Sensu.

optional arguments:
  -h, --help            show this help message and exit
  -l LOG_LEVEL, --log-level LOG_LEVEL
                        [l]og level to use (debug|info|warning|error).
  -s SENSU_URL, --sensu-url SENSU_URL
                        [s]ensu URL to check against
  -S SENSU_PASS, --sensu-pass SENSU_PASS
                        [S]ensu password
  --sensu-user SENSU_USER
                        sensu user
  -c CMDB_URL, --cmdb-url CMDB_URL
                        [c]MDB URL to check against
  -C CMDB_PASS, --cmdb-pass CMDB_PASS
                        [C]MDB password
  --cmdb-user CMDB_USER
                        CMDB user
  -b BATCH_REQUESTS, --batch-requests BATCH_REQUESTS
                        Batch requests fo CMDB (10)
  -t TIMEOUT, --timeout TIMEOUT
                        HTTP request timeout in seconds (60)
  -n DRY_RUN, --dry-run DRY_RUN
                        [d]ry run, do nothing (true|false)
  --verify-ssl VERIFY_SSL
                        [d]ry run, do nothing (true|false)
```