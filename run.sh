#!/usr/bin/env bash

. venv/bin/activate

files="Entradas/graph1.dat Entradas/graph2.dat Entradas/graph3.dat"

for file in $files; do
  python3 DijkstraOddPath.py "$file"
done