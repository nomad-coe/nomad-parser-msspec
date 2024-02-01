#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re
import os
import numpy as np


class MsSpecParser:
    def __init__(self):
        pass

    def parse_system(self):
        pass

    def parse_method(self):
        pass

    def parse_calculation(self):
        pass

    def parse(self, filepath, archive, logger=None):
        self.filepath = filepath
        self.archive = archive
        self.logger = logger

        # Parse input System information
        self.parse_system()

        # Parse input Method information
        self.parse_method()

        # Parse output Calculation information
        self.parse_calculation()
