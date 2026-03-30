# gunicorn.conf.py
import multiprocessing
import os

# Socket binding - use 0.0.0.0 to accept connections from outside the container
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"

# Worker processes - formula: (2 x CPU cores) + 1 [citation:5]
workers = multiprocessing.cpu_count() * 2 + 1

# Worker type - 'sync' is the default and works well for most Django apps
worker_class = 'sync'

# Timeout in seconds - restart workers that hang for this long
timeout = 30

# Maximum requests before worker restart - helps with memory leaks [citation:8]
max_requests = 1000
max_requests_jitter = 50  # Adds randomness to avoid all workers restarting simultaneously

# Log to stdout (Docker-friendly)
accesslog = '-'      # Log to stdout [citation:6]
errorlog = '-'       # Log to stderr
loglevel = 'info'

# Preload app for better memory sharing between workers [citation:8]
preload_app = True

# Set a name for the processes
proc_name = 'Prud-app'