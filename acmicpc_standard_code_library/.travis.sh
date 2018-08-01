#!/bin/bash

set -e

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
CLANG_FORMAT_STYLE=Google
TMP_FILE=/tmp/.tmp

function check_clang_format() {
  local cpp_file
  while read -r cpp_file; do
    echo "checking clang format for $cpp_file"
    clang-format --style=$CLANG_FORMAT_STYLE "$cpp_file" >$TMP_FILE
    if ! diff "$cpp_file" $TMP_FILE; then
      return 1
    fi
  done <<<"$(find . -name '*.cpp')"
}

function check_cpplint() {
  local cpp_file
  while read -r cpp_file; do
    echo "checking cpplint for $cpp_file"
    if ! cpplint "$cpp_file" >/dev/null 2>&1; then
      cpplint "$cpp_file"
      return 1
    fi
  done <<<"$(find . -name '*.cpp')"
}

function check_compile() {
  local cpp_file
  while read -r cpp_file; do
    echo "checking compile for $cpp_file"
    if ! g++-6 "$cpp_file" -o $TMP_FILE >/dev/null 2>&1; then
      g++-6 "$cpp_file" -o $TMP_FILE
      return 1
    fi
  done <<<"$(find . -name '*.cpp')"
}

function check_latex() {
  echo "checking latex..."

  if ! make; then
    return 1
  fi
}

function main() {
  cd "$ROOT_DIR"

  check_clang_format
  check_cpplint
  check_compile

  check_latex
}

main
