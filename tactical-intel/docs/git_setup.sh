#!/bin/bash
# Run this once after cloning to set up all branches
# Usage: bash docs/git_setup.sh

echo "Setting up branches..."

git checkout -b dev
git push -u origin dev

git checkout -b feature/cv-pipeline
git push -u origin feature/cv-pipeline

git checkout -b feature/analytics
git push -u origin feature/analytics

git checkout -b feature/backend
git push -u origin feature/backend

git checkout -b feature/frontend
git push -u origin feature/frontend

git checkout dev
echo ""
echo "All branches created. Everyone should:"
echo "  git fetch --all"
echo "  git checkout feature/<their-branch>"
