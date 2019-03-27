# Github as a Growth Monitor

As part of my Insight Project, I built a data pipeline to monitor Github code eco-system and detect projects depending on vulnerable packages. It could be used by DevOps or SRE team to get when dependent packages have security vulnerability.

## Table of Contents
1. [Introduction](README.md#introduction)  
    * [Product Proposal](product-proposal.md)
2. [Approach](README.md#approach)
3. [Project Structure](README.md#project-structure)
4. [Environment](README.md#Environment)
5. [Run Instructions](README.md#instructions-to-run-the-code)

## Introduction

Git-Monitor is a POC platform to enable organizations to leverage GitHub sort data and track internal package versions along with their dependencies. Recent events like EquiFax Data Breach where attackers exploited a vulnerable library being used by equifax to gain access to critical financial information of millions of people strengthens the importance of organizations to monitor the third party libraries, internal systems depend on.

[Google Slides](https://docs.google.com/presentation/d/17piEWtwxwMT8t5XVfJ0BHs1-1A_t7AkdP_w1gdvQENU/edit#slide=id.g4f145657b5_0_365)  
[Project Link](http://rvsandeep.com/insightproject)

## Approach

## Project Structure
The directory structure for the repo is of following format :
```
      ├── README.md
      ├── execute.sh
      ├── Makefile
      ├── requirements.txt
      ├── src
      │   └──main.py
      │   └──credentials.py
      │   └──jobs
      │       └── create_project_nodes.py
      │       └── create_version_nodes.py
      │       └── create_dependencies.py
      │       └── database_operations.py
      ├── models
      |   └── project.py
      |   └── language.py
      |   └── license.py
      |   └── platform.py
      |   └── status.py
      |   └── version.py
      ├── tests
      ├── libs
      ├── utils
          └── util.py
```

`src/main.py` is the main driver of the application.  
`credentials.py` is used to define NEO4J and AWS access credentials.  
All the spark jobs are placed in `src/jobs` folder.  
The `/models` folder hosts the different data models for neo4j.

## Environment

## Instructions to run the code

## Future Work
