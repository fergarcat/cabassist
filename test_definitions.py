import unittest
from unittest.mock import patch, mock_open, call
import pandas as pd
import time
import user_session as us
import definitions as df

class TestDefinitions(unittest.TestCase):

    @patch('definitions.pd.read_csv')
    def test_get_last_rides_success(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'StartTime': ['10:00:00'],
            'EndTime': ['10:30:00'],
            'DriveMeter': [10],
            'WaitMeter': [5],
            'Fare': [15]
        })
        with patch('builtins.print') as mock_print:
            result = df.get_last_rides()
            self.assertTrue(result)
            mock_print.assert_any_call(f'{df.txt_last_drives}')
            mock_print.assert_any_call(f'{mock_read_csv.return_value}')

    @patch('definitions.pd.read_csv')
    def test_get_last_rides_failure(self, mock_read_csv):
        mock_read_csv.side_effect = Exception("File not found")
        result = df.get_last_rides()
        self.assertFalse(result)

    @patch('builtins.print')
    @patch('definitions.time.time', return_value=1620000000.0)
    def test_display_drive(self, mock_time, mock_print):
        us.currentRide.startTime = 1619996400.0
        us.currentRide.driveMeter = 10
        us.currentRide.waitMeter = 5
        df.display_drive()
        mock_print.assert_called_once_with(
            f'{df.txt_ride_start} {df.formatTime(us.currentRide.startTime)}\n'
            f'{df.txt_current_time} {df.formatTime(mock_time.return_value)}\n'
            f'{df.txt_run_length} {round(us.currentRide.driveMeter, 2)} {df.txt_sec}\n'
            f'{df.txt_wait_length} {round(us.currentRide.waitMeter, 2)} {df.txt_sec}\n'
        )

    def test_total_fare(self):
        us.currentRide.driveMeter = 10
        us.currentRide.waitMeter = 5
        us.drivefee = 2
        us.waitfee = 1
        result = df.total_fare()
        self.assertEqual(result, 25.00)

    @patch('builtins.print')
    def test_display_fees(self, mock_print):
        us.drivefee = 2
        us.waitfee = 1
        df.display_fees()
        mock_print.assert_called_once_with(
            f'{df.txt_current_drive_fee} {us.drivefee}\t{df.txt_current_wait_fee} {us.waitfee}\n'
        )

    def test_formatTime(self):
        t = 1619996400.0
        result = df.formatTime(t)
        self.assertEqual(result, '10:00:00')

    @patch('definitions.pd.DataFrame.to_csv')
    @patch('definitions.os.path.exists', return_value=True)
    @patch('definitions.pd.DataFrame')
    def test_save_data_append(self, mock_DataFrame, mock_exists, mock_to_csv):
        us.currentRide.startTime = 1619996400.0
        us.currentRide.endTime = 1620000000.0
        us.currentRide.driveMeter = 10
        us.currentRide.waitMeter = 5
        us.currentRide.Fare = 15
        df.save_data()
        mock_to_csv.assert_called_once_with('rides.csv', mode='a', header=False, index=False)

    @patch('definitions.pd.DataFrame.to_csv')
    @patch('definitions.os.path.exists', return_value=False)
    @patch('definitions.pd.DataFrame')
    def test_save_data_new_file(self, mock_DataFrame, mock_exists, mock_to_csv):
        us.currentRide.startTime = 1619996400.0
        us.currentRide.endTime = 1620000000.0
        us.currentRide.driveMeter = 10
        us.currentRide.waitMeter = 5
        us.currentRide.Fare = 15
        df.save_data()
        mock_to_csv.assert_called_once_with(us.filename, index=False)

    @patch('definitions.authenticate_user')
    @patch('builtins.input', side_effect=['testuser'])
    @patch('getpass.getpass', side_effect=['password123'])
    def test_login_success(self, mock_getpass, mock_input, mock_authenticate_user):
        mock_authenticate_user.return_value = True
        result = df.login()
        self.assertTrue(result)
        self.assertEqual(us.currentUser, 'testuser')

    @patch('definitions.authenticate_user')
    @patch('builtins.input', side_effect=['testuser'])
    @patch('getpass.getpass', side_effect=['password123'])
    def test_login_failure(self, mock_getpass, mock_input, mock_authenticate_user):
        mock_authenticate_user.return_value = False
        result = df.login()
        self.assertFalse(result)
        self.assertIsNone(us.currentUser)

    @patch('builtins.print')
    @patch('definitions.os.system')
    def test_logo_display(self, mock_system, mock_print):
        df.logo_display()
        mock_system.assert_called_once_with('cls')
        mock_print.assert_has_calls([
            call(f'{df.txt_logo_1}'),
            call(f'{df.txt_logo_2}'),
            call(f'{df.txt_logo_3}'),
            call(f'{df.txt_logo_4}'),
            call(f'{df.txt_logo_5}'),
            call(f'{df.txt_logo_6}'),
            call(f'{df.txt_logo_7}')
        ])

    @patch('builtins.print')
    @patch('time.sleep')
    @patch('builtins.quit')
    def test_exit_program(self, mock_quit, mock_sleep, mock_print):
        df.exit_program()
        mock_print.assert_called_once_with(f'\n\n\t{df.txt_quit}\n\n')
        mock_sleep.assert_called_once_with(3)
        mock_quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()