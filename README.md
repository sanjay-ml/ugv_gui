This repository is a prototype / proof-of-concept demonstrating how a ROS2 node can be integrated with FastAPI in a single Python process.

The goal is not a production-ready system, but a minimal working example that:

Creates a ROS2 node

Exposes ROS telemetry through HTTP endpoints

Sends ROS commands via REST APIs

Shows how FastAPI and ROS2 can run concurrently using threads

Demonstrates basic state sharing and persistence (SQLite)

This code is intended as a foundation to build upon for:

UGV/robot dashboards

ROS2–web bridges

API-driven robot control systems

Expect rough edges — the focus is on architecture experimentation and integration patterns, not optimization or scalability.
