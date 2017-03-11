#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import BOARD, BCM, SUNXI


class sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 12,
        5: 11,
        7: 6,
        8: 198,
        10: 199,
        11: 1,
        12: 7,
        13: 0,
        15: 3,
        16: 19,
        18: 18,
        19: 15,
        21: 16,
        22: 2,
        23: 14,
        24: 13,
        26: 10
    },

    # BCM pin to actual GPIO pin
    BCM: {
        2: 12,
        3: 11,
        4: 6,
        7: 10,
        8: 13,
        9: 16,
        10: 15,
        11: 14,
        14: 198,
        15: 199,
        17: 1,
        18: 7,
        22: 3,
        23: 19,
        24: 18,
        25: 2,
        27: 0
    },

    SUNXI: sunXi()
}


def get_gpio_pin(mode, pin):
    assert mode in [BOARD, BCM, SUNXI]
    return _pin_map[mode][pin]