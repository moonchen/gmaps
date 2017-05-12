PACKAGE = eta_lambda.zip
MODULE_SUBDIR = modules
MODULES += googlemaps

SOURCE_FILES = lambda_function.py direction.py credentials.py model.py route.py
CONFIG_FILE =

all:	$(PACKAGE)

$(PACKAGE):	$(SOURCE_FILES) $(CONFIG_FILE)
	pip3 install --target $(MODULE_SUBDIR) $(MODULES)
	zip -r $(PACKAGE) $(SOURCE_FILES) $(CONFIG_FILE) $(MODULE_SUBDIR)

install:
	aws lambda update-function-code --function-name recordEtaRoute0 --zip-file fileb://$(PACKAGE)

clean:
	$(RM) -r $(MODULE_SUBDIR)
	$(RM) $(PACKAGE)
	$(RM) *.pyc

dist-clean:	clean
	$(RM) $(CONFIG_FILE)

