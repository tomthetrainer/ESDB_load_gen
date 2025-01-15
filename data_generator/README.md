# EventStore Data Generator

This project provides a simple python script to append x number of records to EventStoreDB

## Assumptions

The application assumes an unsecured cluster running locally. 

## Dependencies

The included requirements.txt file can be used to set up your python virtual env. 

Create a venv
`python -m venv .venv`

Activate it
`source .venv/bin/activate`

Or windows powershell Activate

`\venv\Scripts\activate.ps1`

Load dependencies

`pip install -r requirements.txt`

## How to use

To append 100 events, simply run the data_generator.py

`python data_generator.py`

To append a custom number of events.

`python data_generator.py -n 10`

To write the results to a file in addition to the console.

`python data_generator.py -f event_benchmark.txt `

To print help

`python data_generator.py -h`

## Useful Experiments

Compare performance with projections enabled/disabled.

Pass a large number of events through and use to monitor the server load in the dashboard of the webui.

Modify the code and compare performance of secure vs insecure cluster. 

Note we DO NOT recommend running an insecure cluster in production.

Modify the script to batch events in batches of 10, or 100 and compare throughput to non-batched. 

## start_cluster.sh

This is a shell script that will call `docker run` esdb-node, a docker containter that EventStore provides. 

This script was designed for running the code in Github Codespaces, but it will also work on a machine with docker installed.

Note that the start_cluster.sh is designed to refresh the cluster if it has already been started. Running the shell command twice will stop and remove the previous docker instance. 





