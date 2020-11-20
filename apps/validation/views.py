import re
from django.shortcuts import render


class Validation:
    def is_valid_mobile_num(input):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        if input == '':
            return False
        Pattern = re.compile(r"^(0)?9\d{9}$")
        return Pattern.match(input)

    def is_valid_phone_num(input):
        if input == '':
            return False
        Pattern = re.compile(r"^\d{11}$")
        return Pattern.match(input)

    def is_valid_pass(input):
        if input == '':
            return False
        Pattern = re.compile(r"^((?=\S*?[a-zA-Z])(?=\S*?[0-9]).{6,})\S$")
        return Pattern.match(input)

    def is_valid_user_name(input):
        if input == '':
            return False
        Pattern = re.compile(r"^[a-zA-Z0-9]+((_|-|\.)?[a-zA-Z0-9])*$")
        return Pattern.match(input)

    def is_valid_email(input):
        if input == '':
            return False
        Pattern = re.compile(
            r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
        return Pattern.match(input)

    def is_valid_national_code(input):
        if not re.search(r'^\d{10}$', input):
            return False

        check = int(input[9])
        s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
        return (s < 2 and check == s) or (s >= 2 and check + s == 11)

    def is_valid_company_name(input):
        if input == '':
            return False
        Pattern = re.compile(r'^([\u0600-\u06FF\s])+$')
        return Pattern.match(input)

    def is_valid_company_national_number(input):
        if input == '':
            return False
        Pattern = re.compile(r'^[\d]+$')
        return Pattern.match(input)

    def is_valid_farsi_name(input):
        if input == '':
            return False
        Pattern = re.compile(r'^([\u0600-\u06FF\s]{2,20})$')
        return Pattern.match(input)

    def is_valid_farsi_last_name(input):
        if input == '':
            return False
        Pattern = re.compile(r'^([\u0600-\u06FF\s]{2,20})$')
        return Pattern.match(input)

    def is_valid_address(input):
        if input == '':
            return False
        Pattern = re.compile(r'^.{5,200}$')
        return Pattern.match(input)
