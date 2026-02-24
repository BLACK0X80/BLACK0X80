# Setup Guide for BLACK0X80 Profile

## Required Repository Forks
Fork these repos into your GitHub account (BLACK0X80):
- github.com/BLACK0X80/word-cloud → becomes BLACK0X80/word-cloud
- github.com/BLACK0X80/github-stats-terminal-style → BLACK0X80/github-stats-terminal-style
- github.com/BLACK0X80/spotify-github-profile → BLACK0X80/spotify-github-profile (if you want Spotify functionality)

## Required GitHub Secrets
Go to: Settings → Secrets → Actions → New repository secret
- `GH_TOKEN` or `GITHUB_TOKEN`: your GitHub Personal Access Token (classic, with repo + workflow permissions)
- `METRICS_TOKEN`: your GitHub Personal Access Token for the metrics workflow

## Enable GitHub Actions
Go to Actions tab → Enable all workflows

## First Run
After setup, manually trigger each workflow once from the Actions tab.
