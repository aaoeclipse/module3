#!/bin/bash
marco() {
    curr=$(pwd)
    echo "Marco: $curr"
    echo $curr > "/tmp/marco.txt"
}