# The MIT License (MIT)
# Copyright (c) 2016 Postsai
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

class Extension:

    def install_extension_setup(self, config):
        print("Initializing " + __name__)

    def install_print_config_stub(self):
        print("# configuration for " + __name__)

    def install_pre_database_structure_update(self):
        print("Pre database update cleanup for " + __name__)

    def install_post_database_structure_update(self):
        print("Post database update adjustments for " + __name__)
        
    def install_post(self):
        print("Completed install for " + __name__)



    def query_extension_setup(self, config):
        # setup extension on query page
        pass

    def query_create_query(self, postsai, form):
        # may modify postsai.sql and postsai.data
        pass

    def query_post_process_result(self, postsai, form, db, result):
        result["extension"][__name__] = "loaded"
