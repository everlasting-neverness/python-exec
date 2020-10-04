.\Scripts\activate
pyinstaller src/wsgi.py -F `
--name "cfe-os-windows" `
--add-data "src\data\*;data" `
--add-data "src\data\*.jpg;data" `
--hidden-import waitress `
--clean