import multiprocessing

bind = 'unix:/var/www/envapp/.docusys/run/gunicorn.sock'
workers = multiprocessing.cpu_count() * 2