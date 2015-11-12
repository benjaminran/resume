#!/bin/bash

# This isn't necessarily very precise--only gets the last commit
git log --abbrev-commit --pretty=oneline | head -n 1 | cut -d ' ' -f 1
