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
import h5py
import xml.dom.minidom as xmldom  # for pretty generation of XML from the metainfo in hdf5

from nomad.datamodel import EntryArchive
from runschema.run import Run, Program
from runschema.method import Method
from runschema.calculation import Calculation

from xyz_parser import MsSpecXYZParser


class MsSpecParser:
    def __init__(self):
        self.xyz_parser = MsSpecXYZParser()

    def generate_xml(self):
        msspec_metainfo = self.data.get("MsSpec viewer metainfo")
        if msspec_metainfo is None or msspec_metainfo.get("info") is None:
            self.logger.info("MsSpec viewer metainfo cannot be extracted.")
            return
        decoded_msspec_metainfo = [
            bit_string.decode() for bit_string in msspec_metainfo.get("info")
        ]
        msspec_metainfo = "".join(decoded_msspec_metainfo)

        # We store this into a pretty XML generated file
        xml_metainfo = xmldom.parseString(msspec_metainfo)
        pretty_xml_metainfo = xml_metainfo.toprettyxml(indent="\t")
        with open(os.path.join(self.maindir, "msspec_metainfo.xml"), "w") as f:
            f.write(pretty_xml_metainfo)
            self.logger.info("MsSpec metainfo written to XML file.")

    def parse_method(self):
        pass

    def parse_calculation(self):
        pass

    def parse(self, filepath: str, archive: EntryArchive, logger=None):
        self.maindir = os.path.dirname(filepath)
        self.logger = logger

        try:
            data = h5py.File(filepath)
            self.data = data
        except Exception:
            self.logger.error("Error opening hdf5 file.")
            data = None
            return

        sec_run = Run()
        sec_run.program = Program(name="MsSpec")
        # We can generate an XML file from the metainfo in the hdf5 file so that it is easier to read
        self.generate_xml()

        # Parse input System information
        sec_system = self.xyz_parser.parse(filepath, archive, logger)
        sec_run.system.append(sec_system)

        # Parse input Method information
        sec_method = self.parse_method()
        sec_run.method.append(sec_method)

        # Parse output Calculation information
        sec_calc = self.parse_calculation()
        sec_run.calculation.append(sec_calc)

        # Add run section to archive
        archive.run.append(sec_run)
