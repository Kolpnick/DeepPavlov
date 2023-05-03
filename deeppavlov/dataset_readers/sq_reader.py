# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
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

import json
import pickle
from typing import List

from deeppavlov.core.common.registry import register
from deeppavlov.core.data.dataset_reader import DatasetReader
from deeppavlov.core.common.file import load_pickle
from deeppavlov.core.common.file import read_json


@register('sq_reader')
class SQReader(DatasetReader):
    """Class to read training datasets"""

    def read(self, data_path: str, valid_size: int = None):
        if str(data_path).endswith(".pickle"):
            dataset = load_pickle(data_path)
        elif str(data_path).endswith(".json"):
            dataset = read_json(data_path)
        else:
            raise TypeError(f'Unsupported file type: {data_path}')
        if valid_size:
            dataset["valid"] = dataset["valid"][:valid_size]

        return dataset
