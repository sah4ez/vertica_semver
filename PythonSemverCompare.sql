CREATE OR REPLACE LIBRARY SemverCompare AS '/opt/vertica/sdk/python/SemverCompare.py' LANGUAGE 'Python';

CREATE OR REPLACE FUNCTION semverCompare AS NAME 'semver_compare_factory' LIBRARY  SemverCompare;
