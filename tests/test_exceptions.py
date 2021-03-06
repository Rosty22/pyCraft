from minecraft.exceptions import YggdrasilError

import unittest


class RaiseYggdrasilError(unittest.TestCase):
    def test_raise_yggdrasil_error(self):
        with self.assertRaises(YggdrasilError):
            raise YggdrasilError

    def test_raise_yggdrasil_error_message(self):
        with self.assertRaises(YggdrasilError) as e:
            raise YggdrasilError("Error!")

        self.assertEqual(str(e.exception), "Error!")
