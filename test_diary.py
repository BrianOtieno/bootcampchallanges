import unittest, json, diary
from diary import index, register, login, entry, entry_actions, logout

class DiaryTestCase(unittest.TestCase):
#This runs before every test
    def setUp(self):
        print("=*=*=*=*= Preparing Testing Environment =*=*=*=*=")
        diary.app.config['TESTING'] = True
        self.app = diary.app.test_client()

# Tear down after every test.
    def tearDown(self):
        print("=*=*=*=*= Post Testing Routine Tear Down =*=*=*=*=")

    def test_index(self):
        print("==> Running Index Test .....")
        response = self.app.get('/api')
        expected_status_response = "200 OK"
        self.assertEqual(expected_status_response, response.status)

        expected_api_version_message = "200 -OK : API Home: Available API"\
        " Versions [{'2018.24': 'Version 1'}]"
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data["message"], expected_api_version_message)

    def test_register(self):
        print("==> Running Register Test .....")
        response = self.app.get('/api/register')
        #Get POST not defined
        expected_status_response = "404 NOT FOUND"
        self.assertEqual(expected_status_response, response.status)

    def test_login(self):
        pass

    def test_entries(self):
        print("==> Running Entries Test .....")

        response = self.app.get('/api/v1/entries')
        data = json.loads(response.get_data(as_text=True))
        expected_response = {}
        self.assertEqual(expected_response, {})


    def test_entry(self):
        pass

if __name__ == '__main__':
    unittest.main()
