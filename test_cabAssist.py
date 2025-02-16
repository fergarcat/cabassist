import unittest
from unittest.mock import patch, call
import cabAssist as ca
import auth

class TestMenuUsers(unittest.TestCase):

    @patch('cabAssist.menu_display')
    @patch('cabAssist.input')
    @patch('cabAssist.getpass.getpass')
    def test_add_user_success(self, mock_getpass, mock_input, mock_menu_display):
        mock_menu_display.side_effect = ['A', 'M']
        mock_input.side_effect = ['testuser']
        mock_getpass.side_effect = ['password123', 'password123']

        with patch('auth.register_user') as mock_register_user:
            ca.menu_users()
            mock_register_user.assert_called_once_with('testuser', 'password123')
            mock_menu_display.assert_any_call('users')
            mock_menu_display.assert_any_call('wrong')

    @patch('cabAssist.menu_display')
    @patch('cabAssist.input')
    @patch('cabAssist.getpass.getpass')
    def test_add_user_password_mismatch(self, mock_getpass, mock_input, mock_menu_display):
        mock_menu_display.side_effect = ['A', 'M']
        mock_input.side_effect = ['testuser']
        mock_getpass.side_effect = ['password123', 'password456']

        with patch('auth.register_user') as mock_register_user:
            ca.menu_users()
            mock_register_user.assert_not_called()
            mock_menu_display.assert_any_call('wrong')

    @patch('cabAssist.menu_display')
    @patch('cabAssist.input')
    def test_delete_user_confirm(self, mock_input, mock_menu_display):
        mock_menu_display.side_effect = ['D', 'M']
        mock_input.side_effect = ['testuser', 'Y']

        with patch('auth.delete_user') as mock_delete_user:
            ca.menu_users()
            mock_delete_user.assert_called_once_with('testuser')
            mock_menu_display.assert_any_call('users')
            mock_menu_display.assert_any_call('wrong')

    @patch('cabAssist.menu_display')
    @patch('cabAssist.input')
    def test_delete_user_no_confirm(self, mock_input, mock_menu_display):
        mock_menu_display.side_effect = ['D', 'M']
        mock_input.side_effect = ['testuser', 'N']

        with patch('auth.delete_user') as mock_delete_user:
            ca.menu_users()
            mock_delete_user.assert_not_called()
            mock_menu_display.assert_any_call('users')
            mock_menu_display.assert_any_call('wrong')

    @patch('cabAssist.menu_display')
    @patch('cabAssist.input')
    def test_list_users(self, mock_input, mock_menu_display):
        mock_menu_display.side_effect = ['L', 'M']
        mock_input.side_effect = ['']

        with patch('auth.list_users') as mock_list_users:
            ca.menu_users()
            mock_list_users.assert_called_once()
            mock_menu_display.assert_any_call('users')
            mock_menu_display.assert_any_call('wrong')

if __name__ == '__main__':
    unittest.main()