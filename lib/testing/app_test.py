#!/usr/bin/env python3

from os import path
import runpy
import io
import sys

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
       

    def test_app_py_runs(self):
        '''
        is executable
        '''
        
    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        sys.stdout = sys.__stdout__
        
