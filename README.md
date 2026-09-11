# DevSecOps CI/CD Lab

![CI Pipeline](https://github.com/neo-moganedi-tech/devsecops-cicd-lab/actions/workflows/ci.yml/badge.svg)

## Overview

This project demonstrates the implementation of a basic DevSecOps CI/CD pipeline using GitHub Actions

The pipeline automatically validates source code, performs automated testing, executes security analysis, builds the application and deploys the final website

## Architecture

- Developer  
- GitHub Repository  
- GitHub Actions  
- Code Quality Checks  
- Automated Testing    
- Security Analysis  
- Build  
- GitHub Pages Deployment

## CI/CD Pipeline

The CI pipeline performs:

- Source code checkout
- Python environment configuration
- Dependency installation
- Ruff linting
- Pytest automated testing
- Application build
- Build verification

## Security

Security analysis is performed using GitHub CodeQL

The security workflow analyses the Python source code for potential security vulnerabilities

## Deployment

Successful changes to the `main` branch are automatically deployed to GitHub Pages

## Technologies

| Technology | Purpose |
|---|---|
| Git | Version control |
| GitHub | Source code management |
| GitHub Actions | CI/CD automation |
| Python | Application |
| Pytest | Automated testing |
| Ruff | Code quality |
| CodeQL | Security analysis |
| GitHub Pages | Deployment |
| YAML | Pipeline configuration |

## Failure Testing

The pipeline was intentionally tested with a failing unit test to confirm that the CI process correctly detects unsuccessful builds

The test was then corrected and the pipeline successfully returned to a passing state

## Skills Demonstrated

- Continuous Integration
- Continuous Deployment
- DevSecOps
- Automated Testing
- Security Automation
- Git
- GitHub Actions
- YAML
- Python
- CI/CD troubleshooting

## Author

Neo Moganedi
