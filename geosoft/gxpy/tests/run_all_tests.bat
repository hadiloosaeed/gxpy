@set GEOSOFT_TEST_MODE=1
@set GEOSOFT_TESTSYSTEM_MODE=1
call activate py35
python -m unittest
@set GEOSOFT_TEST_MODE=
@set GEOSOFT_TESTSYSTEM_MODE=
