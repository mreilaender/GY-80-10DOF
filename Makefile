# Version must be in the form x.xx, it will be used to locate the dist-packages directory
# You can change this value if you want to use a different version, but 

# all libraries beeing copied, are using version 2.7
PYTHON_VERSION = 2.7

test:
	cd /usr/local/lib/python$(PYTHON_VERSION)/dist-packages
	
install:
	cp -R ./libs/* /usr/local/lib/python$(PYTHON_VERSION)/dist-packages
