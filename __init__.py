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
        """install.py - hook invoked after reading the configuration file"""

        print("Initializing " + __name__)


    def install_print_config_stub(self):
        """install.py - hook invoked to create a stub configuration file"""

        print("# configuration for " + __name__)


    def install_pre_database_structure_update(self):
        """install.py - hook invoked before the database structure is created or updated. 
        Obsolete indexes and views my be deleted here"""

        print("Pre database update cleanup for " + __name__)


    def install_post_database_structure_update(self):
        """install.py - hook invoked after the main database structure has been created or updated. 
        Extension can add additional tables here"""

        print("Post database update adjustments for " + __name__)




    def install_post(self):
        """install.py - hook invoked shortly before install.py is finished"""

        print("Completed install for " + __name__)



    def query_extension_setup(self, config):
        """query-page hook invoked after reading the configuration file"""

        pass


    def query_create_query(self, postsai, form):
        """query-page hook invoked after postsai.sql and postsai.data have been created, but before the statement
           is executed. postsai.sql and postsai.data may be modified at this point"""

        pass


    def query_post_process_result(self, postsai, form, db, result):
        """query-page hook invoked after the database query completed. The result object contains ui-configuration,
        list of repositories, and the actual query results from the database. The result object may be modified here.
        Extension specific information should be communicated to the client in the result["extension"][__name__]
        namespace."""

        result["extension"][__name__] = "loaded"
