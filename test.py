try:
    from app import app
    import unittest
except Exception as e:
    print("Some modules are missing {}".format(e))

class Flasktest(unittest.TestCase):
    # Check for response 200 
    def testcase1(self):
        tester = app.test_client(self)
        resp = tester.get('/get')
        statuscode = resp.status_code
        self.assertEqual(statuscode, 200)

    # Check if the content return is application/json
    def testcase2(self):
        tester = app.test_client(self)
        resp = tester.get('/get')
        self.assertEqual(resp.content_type, "application/json")

    # Check data returned
    def testcase3(self):
        tester = app.test_client(self)
        resp = tester.get('/get')
        self.assertTrue(b'batman' in resp.data)
        
if __name__ == "__main__":
    unittest.main()