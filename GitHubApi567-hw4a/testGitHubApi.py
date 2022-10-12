# start unittest

import unittest
from unittest import mock
import requests
#import mockrequest


# import gitmain class from githubapi.py

from GitHubApi import getCommits, getRepos


class MockResponse:
    def __init__(self, json_data, status_code):
        self.text = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestGitHubApi(unittest.TestCase):
    # Test the getcommits function with mocks

    @mock.patch('requests.get')
    def testGetCommits(self, mocked_req):
        mocked_req.return_value = MockResponse(
            '[{"comdmit": 1}, {"commitd": 1}, {"commit": 2}]', 200)
        response = getCommits("hellogitworld", "richkempinski")

        self.assertEqual(response, 3)

    @mock.patch('requests.get')
    def testGetCommitsFail(self, mocked_reqs):
        mocked_reqs.return_value = MockResponse(
            '[]', 404)
        response = getCommits("hellogitworlddasdasd", "richkempinski")
        self.assertEqual(response, 0)

    def testGetRepos(self):
        self.assertEqual(getRepos("nickd"),
                         [['searchlogic', 30]])

    def testGetReposFail(self):
        self.assertEqual(getRepos("nickdzzdsadadd"), None)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
