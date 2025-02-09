#!/bin/bash

# Store process IDs
declare -a PIDS=()

# Trap Ctrl+C and call cleanup function
cleanup() {
    echo "Cleaning up processes..."
    for PID in "${PIDS[@]}"; do
        kill -9 $PID 2>/dev/null
    done
    exit 0
}
trap cleanup SIGINT SIGTERM

echo "Starting Temporal server..."
temporal server start-dev &
PIDS+=($!)
sleep 2

echo "Starting workflow worker..."
python worker.py Anil &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py Prahastha &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py Ayushman &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py HDFCBank &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py ICICIBank &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py Amazon &
PIDS+=($!)
sleep 1

echo "Starting workflow worker..."
python worker.py Croma &
PIDS+=($!)
sleep 1

# echo "Starting workflow for anil@example.com..."
# python agent_workflow.py anil@example.com &
# PIDS+=($!)
# sleep 1

# echo "Starting workflow for knowledgebot.vendor@example.com..."
# python agent_workflow.py knowledgebot.vendor@example.com &
# PIDS+=($!)
# sleep 1

# echo "Starting workflow for logisticsbot.vendor@example.com..."
# python agent_workflow.py logisticsbot.vendor@example.com &
# PIDS+=($!)

# echo "Starting web server..."
# # python server.py &
# uvicorn server:app --reload --port 8000 &
# PIDS+=($!)

# Wait for Ctrl+C
echo "Press Ctrl+C to stop all processes"
wait
