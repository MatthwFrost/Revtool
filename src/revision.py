#!/usr/bin/env python
from datetime import date, datetime, timedelta
import json

class Revision:
    def __init__(self):
        self.path = '../data/courses.json'
        self.f = open(self.path)
        data = json.load(self.f)
        self.data = data
        self.itr = data['iterate']
        self.current_week = data["current_week"]
        self.TODAY_DATE = date.today()
        self.week_a = [0,3,2,5,4,6,1]
        self.week_b = [0,2,1,3,5,4,6]

    def __del__(self):
        self.f.close()

    def update_itr(self, num):

        if num == 0:
            self.data["iterate"] = 0
        else:
            self.data["iterate"] = self.data["iterate"] + 1

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    # Updates date to todays date when calle
    def update_date(self):
        # Parses json file and assigns the todays date to it
        self.data['courses'][self.itr]['last_accessed'] = str(self.TODAY_DATE)

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


    # Updates date to todays date when called
    def update_week(self):
        # Parses json file and assigns the todays date to it
        self.data['current_week'] = self.current_week

        with open('courses.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def get_revision(self):
        # Random values to call subjects
        week_len = len(self.week_b)

        week_index = [None] * week_len

        # Put current week values into week_index
        if self.current_week == 'week_a':
            for i in range(0, len(self.week_a)):
                week_index[i] = self.week_a[i]
        elif self.current_week == 'week_b':
            # Put week_b values into week_index
            for i in range(0, len(self.week_b)):
                week_index[i] = self.week_b[i]
        

        # Check if iterate has reached 6 then reset and change week
        #print(itr)
        if self.itr == 6:
            self.update_itr(0)

            # Check and swap week values 
            if self.current_week == 'week_a':
                self.current_week = 'week_b'
            elif self.current_week == 'week_b':
                self.current_week = 'week_a'

            self.update_week()

        else: 
            self.update_itr(1)

        itr_num = week_index[self.data['iterate']]
        #print(f"week index: {itr_num}")
        # Use BODMAS to get the subject, brackets first
        subject = (self.data['courses'][itr_num])['subject']
        emoji = (self.data['courses'][itr_num])['emoji']


        # Updating values in db
        # Add back once ready to update data
        self.update_date()

        string = f"{subject} {emoji}"
        return string 

    def get_revisit(self):
        # get date three days ago
        revisit_time = int((self.TODAY_DATE - timedelta(days=3)).strftime('%d'))
        
        for i, d in enumerate(self.data['courses']):
            date = d['last_accessed'][:2]
            if revisit_time == int(date):
                sub_revisit = d['subject']
                break
            else:
                sub_revisit = None

        if sub_revisit is None:
            revisit = "No subject was revised 3 days ago"
            return revisit
        else:
            revisit = f"Revisit: {sub_revisit}"
            return revisit

    def get_week(self):
        return self.data['current_week'].replace("_", " ")[-1:]


