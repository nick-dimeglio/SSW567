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

    def testGetRepos(self):
        self.assertEqual(GitHubApi.getRepos("nickd"),
                         [['searchlogic', 30]])

    def testGetReposFail(self):
        self.assertEqual(GitHubApi.getRepos("nickdzzdsadadd"), None)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
