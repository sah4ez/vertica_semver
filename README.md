# vertica_semver

Python semver comparer for vertica

# install on server

Copy :

```bash
cp -rf ./python /opt/vertica/sdk
cp ./PythonSemverCompare.sql /opt/vertica/sdk
```

# create function

Execute on server this script `./PythonSemverCompare.sql`.

# Usage

Now you can use semver compare with include boundary values.

Description of function:
```
semverCompare(<CURRENT_VERSION>, <FROM_VERSION>, <TO_VERSION>)

-- return Bool
```

Example:
```SQL
create table a(version varchar);
insert into a(version) values ('0.10.1');
insert into a(version) values ('0.0.1');
insert into a(version) values ('0.20.1');
insert into a(version) values ('0.20.12');
select distinct version from a where semverCompare(version, '0.10.0', '0.20.12');
```

Output:
```
version
-------
0.10.1
0.20.1
0.20.12
```
