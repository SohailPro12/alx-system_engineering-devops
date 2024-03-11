### AirBnB Clone Deployment Guide

This repository contains a set of tasks aimed at deploying various versions of the AirBnB clone application onto a server using Python, Flask, Gunicorn, and Nginx.

#### Task 0: Set up development with Python

1. Make sure that task #3 of your SSH project is completed for web-01.
2. Install the net-tools package on your server: `sudo apt install -y net-tools`.
3. Git clone your AirBnB_clone_v2 on your web-01 server.
4. Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.

#### Task 1: Set up production with Gunicorn

1. Install Gunicorn and any other libraries required by your application.
2. Serve the same content from the same route as in the previous task using Gunicorn on web-01, port 5000.

#### Task 2: Serve a page with Nginx

1. Configure Nginx to serve your page from the route `/airbnb-onepage/` both locally and on its public IP on port 80.
2. Proxy requests to the process listening on port 5000.

#### Task 3: Add a route with query parameters

1. Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.

#### Task 4: Serve your AirBnB clone

1. Git clone your AirBnB_clone_v4.
2. Serve content from `web_dynamic/2-hbnb.py` on port 5003 using Gunicorn.
3. Configure Nginx to serve static assets found in `web_dynamic/static/`.
4. Make sure to adjust `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.

#### Task 5: Deploy it!

1. Write a systemd script to start a Gunicorn process serving content from `web_dynamic/2-hbnb.py` with 3 worker processes, logging errors in `/tmp/airbnb-error.log`, and access in `/tmp/airbnb-access.log`.
2. The process should be bound to port 5003.

#### Task 6: No service interruption

1. Write a Bash script to reload Gunicorn in a graceful way, allowing for updates without downtime.

Please refer to the respective directories and files for detailed configurations and scripts related to each task.

**Repository Information:**

- GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- Directory: 0x1A-application_server
