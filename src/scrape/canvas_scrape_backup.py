#!/usr/bin/env python

# Learning how to scrape canvas

import requests
import json

cookies = {
    '_ga': 'GA1.3.1316808209.1623420881',
    'wisepops': '%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A19%2C%22cid%22%3A%2241954%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D',
    'nmstat': 'ad2a5798-fd52-eb7f-d1bf-a8f40b1776eb',
    'wisepops_visits': '%5B%222021-10-14T21%3A52%3A09.629Z%22%2C%222021-06-11T14%3A14%3A40.890Z%22%5D',
    '_gid': 'GA1.3.2113902510.1669140498',
    '_gcl_au': '1.1.819760109.1669140500',
    '_hjid': '0a345d2f-c629-4bc7-8d83-cee32cc26ff2',
    '_fbp': 'fb.2.1669140500513.119948883',
    '_hjSessionUser_881427': 'eyJpZCI6IjUyNTRiMDhkLWIzNTMtNTFlMC04ODJhLWQzMjIzYzU0MjU2ZCIsImNyZWF0ZWQiOjE2NjkxNDA1MDA1MDAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_tt_enable_cookie': '1',
    '_ttp': '15de7465-c282-4a11-b2bd-632c9106157d',
    'LPVID': 'Y0NDlhMGM1NTYyYmI1NThl',
    'LPSID-57489797': 'irYCb5N4QQq4QlYmQ2DWyg',
    '_ga_3G7SKW4487': 'GS1.1.1669140497.1.1.1669140515.0.0.0',
    'log_session_id': 'e4abc41d24d258314fab79f70e6a83f6',
    '_legacy_normandy_session': 'mf8L0Le_x-jdyPNf7KWI9w+a9EJLKcKBUkXT4Gi8f76Gte_AzicUB47Cf12vxH9lfWiyjQZFcUYLz5Ph9OHwAfO8Z3A8fjT249Vz2hFS-b9J2c0cvXhWKX8-hjJVnvg4RPpznnMz4jmK60PP7zNkomjexLdsCv0olWGtXortC7ltbOqOouLAIMluzZt8LP88TsulA_UNDIyuwQBx2iag5kYjitLFK-XNJowtJkf0YosxwPXhoM-zeK4uLNCZX2cyxMZhmGwsezkW7vqDGYdhh3cLmR3d0Xtsiy6O-YT-U5bzrftyj2J3VuxPQf836K3VgMF3KKg9FzE3OvKuWNsYl2JcpP_01hWi13Fc3cN6L3YRed1OtlXFRko73Hmv9JBenAZqhJjtul99bvILy3PJ3HIMnfWo6saSQbI14FGLkJgcIi7Zrqpl5qW8EACpQ0mMh3jV_0dLveV3SQq6X3sms8qPXMMQUOeYtCNSd45UijqtbZBPvzmWfiN0ZbExj8WS0an9an1xKJcuddbhicKm75xWb4Ieg_tJ5-LK6tBiflhkVS2Pso53mWVP_0PBM2cFTM5o8jL6X_y9aVRL85tTfDN.Pf20SDX6FGhdlQd_I6ZnoTpDzF4.Y31G7g',
    'canvas_session': 'mf8L0Le_x-jdyPNf7KWI9w+a9EJLKcKBUkXT4Gi8f76Gte_AzicUB47Cf12vxH9lfWiyjQZFcUYLz5Ph9OHwAfO8Z3A8fjT249Vz2hFS-b9J2c0cvXhWKX8-hjJVnvg4RPpznnMz4jmK60PP7zNkomjexLdsCv0olWGtXortC7ltbOqOouLAIMluzZt8LP88TsulA_UNDIyuwQBx2iag5kYjitLFK-XNJowtJkf0YosxwPXhoM-zeK4uLNCZX2cyxMZhmGwsezkW7vqDGYdhh3cLmR3d0Xtsiy6O-YT-U5bzrftyj2J3VuxPQf836K3VgMF3KKg9FzE3OvKuWNsYl2JcpP_01hWi13Fc3cN6L3YRed1OtlXFRko73Hmv9JBenAZqhJjtul99bvILy3PJ3HIMnfWo6saSQbI14FGLkJgcIi7Zrqpl5qW8EACpQ0mMh3jV_0dLveV3SQq6X3sms8qPXMMQUOeYtCNSd45UijqtbZBPvzmWfiN0ZbExj8WS0an9an1xKJcuddbhicKm75xWb4Ieg_tJ5-LK6tBiflhkVS2Pso53mWVP_0PBM2cFTM5o8jL6X_y9aVRL85tTfDN.Pf20SDX6FGhdlQd_I6ZnoTpDzF4.Y31G7g',
    '_csrf_token': 'DF1VsYJo7qvuhobofmVkyW8w2dBhhFC5yV5STm4uttplM3rw1hnFwri0s7ItUBHiNwmwlyDeA9u4OTYAJ2%2BC4w%3D%3D',
}

headers = {
    'authority': 'canvas.swansea.ac.uk',
    'accept': 'application/json+canvas-string-ids, application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/"7a7b5e55ec0cda7c5cfe9779bf67ef3e"',
    'referer': 'https://canvas.swansea.ac.uk/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get('https://canvas.swansea.ac.uk/api/v1/dashboard/dashboard_cards', cookies=cookies, headers=headers)
data = response.json()

substring = "2223"

for i in data:
    if substring in i['longName']:
        print(i['longName'])
