﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'метро':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'сильпо':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
    ],
    'карамель': [
        {'shop': 'сильпо', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99}
    ],
    'печенье': [
        {'shop': 'метро', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99}
    ],
    'конфеты': [
        {'shop': 'сильпо', 'price': 30.99},
        {'shop': 'метро', 'price': 32.99}
    ],
    'пирожное': [
        {'shop': 'метро', 'price': 59.99},
        {'shop': 'сильпо', 'price': 62.99}
    ],
}
# Указать надо только по 2 магазина с минимальными ценами
print(sweets['карамель'])
print(sweets['печенье'])
print(sweets['пирожное'])
print(sweets['конфеты'])


$ НОРМАС!




