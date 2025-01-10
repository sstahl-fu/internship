#!/usr/bin/env python3
"""
Created on Fri Sep 27 09:08:03 2024

@author: a2853
"""

#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
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

import os

from nomad.datamodel import EntryArchive
from nomad.datamodel.data import EntryData
from nomad.metainfo import Quantity
from nomad.parsing import MatchingParser


class SolarTabRawFile(EntryData):
    data_file = Quantity(
        type=str,
        a_browser=dict(adaptor='RawFileAdaptor'),
    )


class SolarTabSimulationParser(MatchingParser):
    def parse(self, mainfile: str, archive: EntryArchive, logger):
        archive.data = SolarTabRawFile(data_file=os.path.basename(mainfile))
