import unittest
import pathlib
import re

PRESETS_FILE_NAME = "external/presets.py"


class ParaboxTest(unittest.TestCase):
    def test_preset_format(self):
        file = (pathlib.Path(__file__).parent.parent / PRESETS_FILE_NAME).resolve()
        with file.open("r") as file:
            lines = file.read().split("\n")
            idx: int
            line: str
            for idx, line in enumerate(lines):
                match = re.match(r".*\"([^\"]*)\"\s*:\s*([^.]*)\..*", line)
                if match is None:
                    continue

                (first, second) = match.groups()
                message = (f"Invalid matchup of option values in preset definition \"{first}\" and \"{second}\""
                           f" ({PRESETS_FILE_NAME}:{idx+1})\n\t{line}")
                self.assertTrue(second.endswith("Values"), message)
                second2 = re.sub(r"Values$", "", second)
                self.assertEqual(first.replace("_",""), second2.lower(), message)
