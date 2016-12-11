![Logo](https://raw.githubusercontent.com/postsai/postsai/master/resources/postsai-64.png) Postsai Extension Stub
-------

[Postsai](https://postsai.github.io/) is a queriable database for source control commit.

You can use this project as a template to extend Postsai with additional functionality.

Installation and configuration
-
- Postsai extensions are installed by copying them as folder to the `extensions` directory.
- Some extension require you to execute `./install.py` in the Postsai root folder.
- Postsai extensions are typically configured using the standard `config.py` file. Please refer to the documentation of the concrete extension for details.

Information for Developers
-
From Pythons point of view, each Postsai extension is a Python package. Therefore it needs the standard Python package file `__init__.py`.

Postsai looks for an exported class called `Extension` in `__init__.py`.  The methods of this class are called as extension points. This exampe extension implements all known extensions points for documentation purposes. Normal extension will only define the methods, they are interested in.

Please refer to [`__init__.py`](https://github.com/postsai/extensionstub/blob/master/__init__.py#L24) for the documentation of all extension points.

If an extension provides a file called `query.js` it will be loaded and executed by the browser after the api call completed.

Please include LICENSE.txt and README.md in your extension with appropriate content to make it easy for the users of your extension.


Legal
-
(C) Copyright 2016 Postsai. Postsai is released as Free and Open Source Software under [MIT](https://raw.githubusercontent.com/postsai/postsai/master/LICENSE.txt) license.

