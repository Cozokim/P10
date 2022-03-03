#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "13ff1d0f-a381-490b-ab47-fc52d5e335b9")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Cestlemotdepassecompliqué*")
