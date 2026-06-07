import unittest
from verification.harness.pascal_module_extractor import extract_pascal_module_sequence
import tempfile
import os

class TestPascalModuleExtractor(unittest.TestCase):
    def test_extract_sequence(self):
        content = """
        {1:}
        program TEST;
        {2:}
        begin
        {:2}
        end.
        {:1}
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.p', delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            sequence = extract_pascal_module_sequence(temp_path)
            self.assertEqual(len(sequence), 4)
            self.assertEqual(sequence[0], {'type': 'start', 'module': 1, 'pos': content.find('{1:}')})
            self.assertEqual(sequence[1], {'type': 'start', 'module': 2, 'pos': content.find('{2:}')})
            self.assertEqual(sequence[2], {'type': 'end', 'module': 2, 'pos': content.find('{:2}')})
            self.assertEqual(sequence[3], {'type': 'end', 'module': 1, 'pos': content.find('{:1}')})
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_no_markers(self):
        content = "program TEST; begin end."
        with tempfile.NamedTemporaryFile(mode='w', suffix='.p', delete=False) as f:
            f.write(content)
            temp_path = f.name

        try:
            sequence = extract_pascal_module_sequence(temp_path)
            self.assertEqual(len(sequence), 0)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
