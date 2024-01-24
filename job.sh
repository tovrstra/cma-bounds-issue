#!/usr/bin/env bash
#SBATCH --job-name=bounds
#SBATCH --mem=5g
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=72:00:00

source venv/bin/activate
date
time python bounds.py
date
