#!/bin/bash
prefect cloud login --key $1 --workspace $2
prefect agent start -q $3