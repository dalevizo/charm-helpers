# Copyright 2016 Canonical Limited.
#
# This file is part of charm-helpers.
#
# charm-helpers is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3 as
# published by the Free Software Foundation.
#
# charm-helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with charm-helpers.  If not, see <http://www.gnu.org/licenses/>.
from charmhelpers.contrib.hardening.host.checks import (
    run_os_checks,
)
from charmhelpers.core.hookenv import (
    log,
    INFO,
    config,
)


def harden_os():
    log("Hardening OS", level=INFO)
    run_os_checks()
    log("OS hardening complete", level=INFO)


def dec_harden_os(f):
    if config('harden'):
        harden_os()

    def _harden_os(*args, **kwargs):
        return f(*args, **kwargs)

    return _harden_os


# Run on import
if config('harden'):
    harden_os()
