import hashlib, json, requests
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
from src.routes import app
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 run.py [PORT]")
        exit()
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
