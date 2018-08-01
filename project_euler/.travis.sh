#!/bin/bash

set -e

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
CLANG_FORMAT_STYLE=Google
PYLINTRC=./.pylintrc
TMP_FILE=/tmp/.tmp

function check_clang_format() {
  local cc_file
  while read -r cc_file; do
    echo "checking clang format for $cc_file"
    clang-format --style=$CLANG_FORMAT_STYLE "$cc_file" >$TMP_FILE
    if ! diff "$cc_file" $TMP_FILE; then
      return 1
    fi
  done <<<"$(find . -name '*.cc')"
}

function check_cpplint() {
  local cc_file
  while read -r cc_file; do
    echo "checking cpplint for $cc_file"
    if ! cpplint "$cc_file" >/dev/null 2>&1; then
      cpplint "$cc_file"
      return 1
    fi
  done <<<"$(find . -name '*.cc')"
}

function check_gofmt() {
  local go_file
  while read -r go_file; do
    echo "checking gofmt for $go_file"
    gofmt "$go_file" >$TMP_FILE
    if ! diff "$go_file" $TMP_FILE; then
      return 1
    fi
  done <<<"$(find . -name '*.go')"
}

function check_golint() {
  local go_file
  while read -r go_file; do
    echo "checking golint for $go_file"
    if ! golint --set_exit_status "$go_file" >/dev/null 2>&1; then
      golint --set_exit_status "$go_file"
      return 1
    fi
  done <<<"$(find . -name '*.go')"
}

function check_yapf() {
  local py_file
  while read -r py_file; do
    echo "checking yapf for $py_file"
    yapf "$py_file" >$TMP_FILE
    if ! diff "$py_file" $TMP_FILE; then
      return 1
    fi
  done <<<"$(find . -name '*.py')"
}

function check_pylint() {
  local py_file
  while read -r py_file; do
    echo "checking pylint for $py_file"
    if ! pylint --rcfile=$PYLINTRC "$py_file" >/dev/null 2>&1; then
      pylint --rcfile=$PYLINTRC "$py_file"
      return 1
    fi
  done <<<"$(find . -name '*.py')"
}

function check_answers() {
  echo "checking answers..."
  ./run_all.sh
  ./run_all.sh >$TMP_FILE
  if ! diff ./answers.txt $TMP_FILE; then
    return 1
  fi
}

function main() {
  cd "$ROOT_DIR"

  check_clang_format
  check_cpplint

  check_gofmt
  check_golint

  check_yapf
  check_pylint

  check_answers
}

main
