#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import webbrowser

class VK:

    def __init__(self, permissions: tuple, app_id: str, api_version: str='5.124'):

        self.client_id = app_id
        self.scope = permissions
        self.api_v = api_version
        self.response = None
        self.access_token = None
        self.user_id = None

    def authorize(self):
        api_auth_url = 'https://oauth.vk.com/authorize'
        redirect_uri = 'https://oauth.vk.com/blank.html'
        response_type = 'token'
        display = 'page'
        url = '{}?client_id={}&scope={}&redirect_uri={}&display={}&v={}&response_type={}'
        url = url.format(api_auth_url, self.client_id, ','.join(self.scope), redirect_uri,
                         display, self.api_v, response_type)
        webbrowser.open(url, new=2, autoraise=True)
        self.access_token = input('Please, accept permissions and enter your token: ')

    def post(self, text):
        url = (f'https://api.vk.com/method/wall.post?'
               f'message={text}&access_token={self.access_token}&v={self.api_v}')
        try:
            request = requests.get(url)
            response = request.json()
            print(f'Your message successfully posted, post id: '
                  f'{response["response"]["post_id"]}')
        except:
            print(f'Some error occupied.')

    def message(self):
        text = input('Enter your message: ')
        if len(text) > 140:
            print('The message length must not exceed 140 characters.')
        else:
            self.post(text)


if __name__ == '__main__':
    vk = VK(('wall',), '')
    vk.authorize()
    vk.message()