#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
# yjdsq

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

a1, a2 = sites['Moscow']
b1, b2 = sites['London']
c1, c2 = sites['Paris']
m_l = int(((a1-b1)**2 + (a2-b2)**2) **0.5)
m_p = int(((a1-c1)**2 + (a2-c2)**2) **0.5)
p_l = int(((c1-b1)**2 + (c2-b2)**2) **0.5)

distances = {m_l,m_p,p_l}

# completed

print(distances)




