#!/bin/bash
echo "======= Changes detected - Compiling ======="
kotlinc solve.kt -include-runtime -d solve.jar
echo "==== Run ===="
kotlin solve.jar