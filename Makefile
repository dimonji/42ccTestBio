ENV_BIN = ${HOME}/bin
HOME = ${shell pwd}
PYTHON = ${HOME}/bin/python
PROJECT = ${HOME}/src

buildenv:
	virtualenv --no-site-packages ${HOME}
	bin/pip install -E ./ -r ./requirements.txt

clean:
	-rm -rf bin
	-rm -rf lib
	-rm -rf include
	-rm -rf man
	-rm -rf *~*
	-rm -rf *#*
	-find . -name '*.pyc' -exec rm {} \;
	rm -f ${PROJECT}/test_bio

test:	clean	buildenv	syncdb	pep8
	DJANGO_SETTINGS_MODULE=settings PYTHONPATH=.:src ${PYTHON} ${ENV_BIN}/nosetests

syncdb:
	${PYTHON} ${HOME}/src/manage.py syncdb --noinput

run:
	${PYTHON} ${PROJECT}/manage.py runserver 0.0.0.0:8088

pep8:
	${ENV_BIN}/pep8 --filename=*.py --ignore=W --exclude="manage.py,settings.py" --statistics --repeat ${PROJECT}
