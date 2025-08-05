# test_heartbeat.py
"""
Tests for HeartBeat module.
"""

import unittest
from heartbeat import HeartBeat

class TestHeartBeat(unittest.TestCase):
    """Test cases for HeartBeat class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HeartBeat()
        self.assertIsInstance(instance, HeartBeat)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HeartBeat()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
