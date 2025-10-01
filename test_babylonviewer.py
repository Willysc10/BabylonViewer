# test_babylonviewer.py
"""
Tests for BabylonViewer module.
"""

import unittest
from babylonviewer import BabylonViewer

class TestBabylonViewer(unittest.TestCase):
    """Test cases for BabylonViewer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BabylonViewer()
        self.assertIsInstance(instance, BabylonViewer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BabylonViewer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
