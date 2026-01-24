This repository is a prototype demonstrating how a ROS2 node can be integrated with FastAPI in a single Python process.
The goal is not a production-ready system, but a minimal working example that:
    1) Creates a ROS2 node
    2) Exposes ROS telemetry through HTTP endpoints
    3) Sends ROS commands via REST APIs
    4) Shows how FastAPI and ROS2 can run concurrently using threads
    5) Demonstrates basic state sharing and persistence (SQLite)

This code is intended as a foundation to build upon for:
    1) UGV/robot dashboards
    2) ROS2–web bridges
    3) API-driven robot control systems

Expect rough edges — the focus is on architecture experimentation and integration patterns, not optimization or scalability.
