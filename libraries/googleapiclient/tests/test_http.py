#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Http tests

Unit tests for the apiclient.http.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

# Do not remove the httplib2 import
import httplib2
import unittest

from apiclient.http import set_user_agent
from apiclient.http import HttpMockSequence


class TestUserAgent(unittest.TestCase):

  def test_set_user_agent(self):
    http = HttpMockSequence([
      ({'status': '200'}, 'echo_request_headers'),
      ])

    http = set_user_agent(http, "my_app/5.5")
    resp, content = http.request("http://example.com")
    self.assertEqual(content['user-agent'], 'my_app/5.5')

  def test_set_user_agent_nested(self):
    http = HttpMockSequence([
      ({'status': '200'}, 'echo_request_headers'),
      ])

    http = set_user_agent(http, "my_app/5.5")
    http = set_user_agent(http, "my_library/0.1")
    resp, content = http.request("http://example.com")
    self.assertEqual(content['user-agent'], 'my_app/5.5 my_library/0.1')

if __name__ == '__main__':
  unittest.main()
