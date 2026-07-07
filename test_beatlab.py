# test_beatlab.py
"""
Tests for BeatLab module.
"""

import unittest
from beatlab import BeatLab

class TestBeatLab(unittest.TestCase):
    """Test cases for BeatLab class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeatLab()
        self.assertIsInstance(instance, BeatLab)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeatLab()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
