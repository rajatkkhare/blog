#!/bin/bash
gunicorn --workers 3 --preload --bind 0.0.0.0:5000 wsgi:application