Email Pixel Tracker

A microservice-based tracking system that logs email "open" events using an invisible 1x1 pixel. Built to demonstrate intermediate container orchestration and backend integration.
How it works

    FastAPI serves a transparent 1x1 PNG at the /track/{id} endpoint.

    Redis acts as a high-speed counter for real-time analytics.

    PostgreSQL (In Progress) handles long-term persistence and metadata logging.

Docker Features Implemented

    Multi-Service Orchestration: Uses Docker Compose to manage the app, cache, and database on a shared internal network.

    Healthchecks: The web service waits for the PostgreSQL container to be fully "Healthy" (not just "Started") before attempting to connect.

    Volume Persistence: Database data is mapped to a named volume to ensure tracking history survives container restarts.

    Optimized Builds: Uses python-slim as a base image to reduce footprint.

Tech Stack

    Backend: Python 3.11 + FastAPI

    Cache: Redis

    Database: PostgreSQL 15

    Environment: WSL2 / Ubuntu

Usage

    Clone and Build:
    Bash

    git clone <your-repo-url>
    cd email-pixel-tracker
    docker compose up --build

    Test the Tracker: Open http://localhost:8000/track/test-campaign in your browser.

    Check Stats: Visit http://localhost:8000/stats/test-campaign to see the open count.
