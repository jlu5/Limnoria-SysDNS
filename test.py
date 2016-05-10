###
# Copyright (c) 2014-2016, James Lu <glolol@overdrivenetworks.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###
import os

from supybot.test import *
from supybot import conf

class SysDNSTestCase(PluginTestCase):
    plugins = ('SysDNS',)

    # Make the 'host' binary that should be used configurable. This is useful in
    # Travis-CI for example, where bind9-host (/usr/bin/host) isn't available, but
    # unbound-host is via /usr/bin/unbound-host.
    host_cmd = os.environ.get('SYSDNS_HOST_COMMAND', conf.supybot.plugins.SysDNS.command())

    config = {'supybot.plugins.SysDNS.command': host_cmd}

    print('SysDNS: using %r as host binary' % host_cmd)
    
    def testBasics(self):
        self.assertNotError('sysdns dns google.com')
        self.assertRegexp('sysdns dns localhost', '127\.0\.0\.1')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
