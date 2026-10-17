# test_centernaga.py
"""
Tests for CenterNaga module.
"""

import unittest
from centernaga import CenterNaga

class TestCenterNaga(unittest.TestCase):
    """Test cases for CenterNaga class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CenterNaga()
        self.assertIsInstance(instance, CenterNaga)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CenterNaga()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
