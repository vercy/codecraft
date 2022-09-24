#!/usr/bin/env python3
import os

import aws_cdk as cdk

from python_http.python_http_stack import PythonHttpStack

app = cdk.App()
PythonHttpStack(app, "PythonHttpStack",
                env=cdk.Environment(account='123456789012', region='us-east-1')
                )

app.synth()
