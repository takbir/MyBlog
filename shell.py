# -*- coding: utf-8 -*-

import sys
import os
import settings

packages_path = os.path.join(settings.SITE_ROOT, 'packages')

sys.path.insert(0, packages_path)
