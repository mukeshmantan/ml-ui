#!/usr/bin/env python
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
# -*- coding: utf-8 -*-
"""
Provides a "talker" application that sends iris DataFrame protobuf messages
"""
import argparse
import time

import requests
from sklearn.datasets import load_iris

from acumos.wrapped import load_model


if __name__ == '__main__':
    '''Main'''

    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", default='http://127.0.0.1:3330/transform')
    parser.add_argument("--sleep", default=5)
    parser.add_argument("--modeldir", type=str, default='model')
    parser.add_argument("--csvdata", type=str, default='')
    pargs = parser.parse_args()

    model = load_model(pargs.modeldir)  # refers to ./model dir in pwd. generated by helper script also in this dir

    if pargs.csvdata:
        import pandas as pd
        dfRaw = pd.read_csv(pargs.csvdata)
        X = dfRaw.as_matrix()
    else:
        iris = load_iris()
        X = iris.data

    # build protobuf message that model consumes
    DataFrame = model.transform.pb_input_type

    X_msg = DataFrame()
    for col, field in enumerate(DataFrame.DESCRIPTOR.fields):
        getattr(X_msg, field.name).extend(X[:, col].tolist())

    X_bytes = X_msg.SerializeToString()

    # eat errors and talk forever
    while True:
        try:
            requests.post(pargs.uri, data=X_bytes)
        except Exception as e:
            print("[ERROR] {}".format(e))
        finally:
            time.sleep(pargs.sleep)
