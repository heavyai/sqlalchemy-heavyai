"""
OmniSci engine for Apache Superset.

Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
from datetime import datetime
from typing import TYPE_CHECKING, List, Optional, Tuple

from superset.db_engine_specs.base import BaseEngineSpec, LimitMethod

if TYPE_CHECKING:
    # prevent circular imports
    from superset.models.core import Database  # noqa: F401


class OmniSciEngineSpec(BaseEngineSpec):
    """Apache Superset Engine for OmniSci."""

    engine = "omnisci"
    engine_name = "OmniSci"

    _time_grain_functions = {
        None: "{col}",
        "PT1S": "DATE_TRUNC(second, {col})",
        "PT1M": "DATE_TRUNC(minute, {col})",
        "PT1H": "DATE_TRUNC(hour, {col})",
        "P1D": "DATE_TRUNC(day, {col})",
        "P1W": "DATE_TRUNC(week, {col})",
        "P1M": "DATE_TRUNC(month, {col})",
        "P0.25Y": "DATE_TRUNC(quarter, {col})",
        "P1Y": "DATE_TRUNC(year, {col})",
    }

    def __init__(self, *args, **kwargs):
        """Instantiate OmniSciEngineSpec."""
        print("using omnisci backend")
        print(args, kwargs)
        super().__init__(*args, **kwargs)

    @classmethod
    def fetch_data(cls, cursor, limit: Optional[int] = None) -> List[Tuple]:
        """Fetch data."""
        if not cursor.description:
            return []
        if cls.limit_method == LimitMethod.FETCH_MANY:
            return cursor.fetchmany(limit)
        return cursor.fetchall()

    @classmethod
    def epoch_to_dttm(cls) -> str:
        """Epoch to datetime."""
        return "(timestamp 'epoch' + {col} * interval '1 second')"

    @classmethod
    def convert_dttm(cls, target_type: str, dttm: datetime) -> str:
        """Convert datetime."""
        return "'{}'".format(dttm.strftime("%Y-%m-%d %H:%M:%S"))
