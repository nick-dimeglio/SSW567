# start unittest
import unittest
import GitHubApi


class TestGitHubApi(unittest.TestCase):
    def testGetCommits(self):
        self.assertEqual(GitHubApi.getCommits(
            "hellogitworld", "richkempinski"), 30)

    def testGetCommitsFail(self):
        self.assertEqual(GitHubApi.getCommits(
            "hellogitworldzz", "richkempinski"), 0)
