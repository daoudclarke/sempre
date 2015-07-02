#!/bin/bash
#

# ===========================================
# Parameters for Sun Grid Engine submition
# ============================================

# Name of job
#$ -N parasempre

# Shell to use
#$ -S /bin/bash

# All paths relative to current working directory
#$ -cwd

# List of queues
# #$ -q serial.q
#$ -q 'nlp-amd,serial.q,inf.q,eng-inf_parallel.q'

# Define parallel environment for multicore processing
#$ -pe openmp 1

# Send mail to. (Comma separated list)
#$ -M dc34@sussex.ac.uk

# When: [b]eginning, [e]nd, [a]borted and reschedules, [s]uspended, [n]one
#$ -m beas

# Validation level (e = reject on all problems)
#$ -w e

# Merge stdout and stderr streams: yes/no
#$ -j yes

module add jdk/1.7.0_51_openjdk

java -version

echo 'Beginning processing'

PYTHONPATH=../sexpdata/ python parselog.py trans_state/execs/12.exec/log

echo 'Processing complete'

