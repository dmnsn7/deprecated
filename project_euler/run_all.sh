#!/bin/bash

set -e

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

function get_prob_id() {
  echo "$1" | awk -F '/' '{print $NF}' | awk -F '.' '{print $1}'
}

function method_cc() {
  pushd "$(dirname "$1")" >/dev/null 2>&1
  local prob_id ans_file data_file
  prob_id=$(get_prob_id "$1")
  cc_file=./$prob_id.cc
  ans_file=./$prob_id.cc.ans
  bin_file=./$prob_id.cc.bin
  data_file=./$prob_id.data
  if [[ ! -f $ans_file ]]; then
    g++-6 "$cc_file" -o "$bin_file"
    if [[ ! -f $data_file ]]; then
      $bin_file >"$ans_file"
    else
      $bin_file <"$data_file" >"$ans_file"
    fi
    rm "$bin_file"
  fi
  echo "Problem_$prob_id CC: $(cat "$ans_file")"
  popd >/dev/null 2>&1
}

function method_py() {
  pushd "$(dirname "$1")" >/dev/null 2>&1
  local prob_id ans_file data_file
  prob_id=$(get_prob_id "$1")
  py_file=./$prob_id.py
  ans_file=./$prob_id.py.ans
  data_file=./$prob_id.data
  if [[ ! -f $ans_file ]]; then
    if [[ ! -f $data_file ]]; then
      $py_file >"$ans_file"
    else
      $py_file <"$data_file" >"$ans_file"
    fi
  fi
  echo "Problem_$prob_id PY: $(cat "$ans_file")"
  popd >/dev/null 2>&1
}

function method_go() {
  pushd "$(dirname "$1")" >/dev/null 2>&1
  local prob_id ans_file data_file
  prob_id=$(get_prob_id "$1")
  go_file=./$prob_id.go
  ans_file=./$prob_id.go.ans
  data_file=./$prob_id.data
  if [[ ! -f $ans_file ]]; then
    if [[ ! -f $data_file ]]; then
      go run "$go_file" >"$ans_file"
    else
      go run "$go_file" <"$data_file" >"$ans_file"
    fi
  fi
  echo "Problem_$prob_id GO: $(cat "$ans_file")"
  popd >/dev/null 2>&1
}

function main() {
  cd "$ROOT_DIR"

  local src_file
  while read -r src_file; do
    if [[ "$src_file" =~ .*cc$ ]]; then
      method_cc "$src_file"
    elif [[ "$src_file" =~ .*go$ ]]; then
      method_go "$src_file"
    elif [[ "$src_file" =~ .*py$ ]]; then
      method_py "$src_file"
    fi
  done <<<"$(find . | grep -v '/.git/' | grep -E 'cc$|go$|py$')"
}

main
