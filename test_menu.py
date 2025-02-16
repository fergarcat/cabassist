import unittest
from unittest.mock import patch
import menu as mn

class TestMenuDisplay(unittest.TestCase):

    @patch('menu.logo_display')
    @patch('menu.input')
    @patch('menu.login')
    @patch('menu.exit_program')
    def test_menu_welcome_successful_login(self, mock_exit_program, mock_login, mock_input, mock_logo_display):
        mock_login.return_value = True
        mock_input.return_value = ''
        mn.menu_display('welcome')
        mock_logo_display.assert_called()
        mock_login.assert_called()
        mock_input.assert_called_with()
        mock_exit_program.assert_not_called()

    @patch('menu.logo_display')
    @patch('menu.input')
    @patch('menu.login')
    @patch('menu.exit_program')
    def test_menu_welcome_failed_login(self, mock_exit_program, mock_login, mock_input, mock_logo_display):
        mock_login.return_value = False
        mock_input.return_value = ''
        mn.menu_display('welcome')
        self.assertEqual(mock_login.call_count, 3)
        mock_exit_program.assert_called_once()

if __name__ == '__main__':
    unittest.main()