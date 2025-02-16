import unittest
from unittest.mock import patch, mock_open
import auth

class TestAuth(unittest.TestCase):

    @patch('auth.os.path.exists')
    @patch('auth.open', new_callable=mock_open, read_data='{}')
    def test_load_users_file_exists(self, mock_file, mock_exists):
        mock_exists.return_value = True
        users = auth.load_users()
        mock_file.assert_called_once_with(auth.USER_DB, 'r')
        self.assertEqual(users, {})

    @patch('auth.os.path.exists')
    @patch('auth.open', new_callable=mock_open)
    def test_load_users_file_not_exists(self, mock_file, mock_exists):
        mock_exists.return_value = False
        users = auth.load_users()
        mock_file.assert_not_called()
        self.assertEqual(users, {})

if __name__ == '__main__':
    unittest.main()