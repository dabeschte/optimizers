"""
Copyright (c) Meta Platforms, Inc. and affiliates.
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

"""

import re
import unittest

from dataclasses import dataclass

from commons import AbstractDataclass


@dataclass(init=False)
class DummyOptimizerConfig(AbstractDataclass):
    """Dummy abstract dataclass for testing. Instantiation should fail."""


class InvalidAbstractDataclassInitTest(unittest.TestCase):
    def test_invalid_init(self) -> None:
        for abstract_cls in (
            AbstractDataclass,
            DummyOptimizerConfig,
        ):
            with self.subTest(abstract_cls=abstract_cls):
                self.assertRaisesRegex(
                    TypeError,
                    re.escape(
                        f"Can't instantiate abstract class {abstract_cls.__name__} with abstract method __init__"
                    ),
                    abstract_cls,
                )
