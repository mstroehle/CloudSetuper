#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from basehandlers import BaseHandler


class IndexHandler(BaseHandler):

    @authenticated
    def get(self):
        print self.dbSession, '+++++++', self.current_user
        if not self.current_user:  
            self.redirect("/login")  
            return
        self.render("index.html", title="Cloud Setuper")

    def post(self):
        softwarename = self.get_argument("softwarename", "")
        softwareauthor = self.get_argument("softwareauthor", "")
        softwareemail = self.get_argument("softwareemail", "")
        softwarecompany = self.get_argument("softwarecompany", "")
        software = {
            'softwarename': softwarename,
            'softwareauthor': softwareauthor,
            'softwareemail': softwareemail,
            'softwarecompany': softwarecompany,
        }
        print software
        flag = self.onesetup(software)
        response = {
            'status': "success"
        }
        self.write(response)

    def onesetup(self, software):
    	print "onesetup==================="
