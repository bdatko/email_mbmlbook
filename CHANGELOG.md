## 0.2.0 (2022-03-26)

### Fix

- **email_mbmlbook/data.py**: hand edge case for users do not have feature set
- **email_mbmlbook/data.py**: add flag to use feature set from a user
- **email_mbmlbook/data.py**: sort multiple values before storing
- **email_mbmlbook/data.py**: change int() to float() for double
- **tests/test_data.py**: correct unique values for Recipient and correct dist values for repliedTo
- **email_mbmlbook/data.py**: add varying parsing if there is either missing, expected, or multiple values

### Feat

- **email_mbmlbook/data.py**: add flag to validate feature sets across users
- **email_mbmlbook/data.py**: generalize parsing of objml baed on parsing Inital, Compound, and OneFeature
- **initial.py**: first iteration of parsing InitialInputs.objml
- **compound.py**: add first iteratoin of parsing CompoundInputs.objml
- **email_mbmlbook/__init__.py**: add FeatureSet to package imports
- **email_mbmlbook**: add FeatureSet class for parsing objml files
- **single.py**: first iteratoin of parsing OneFeatureInputs.objml

### Refactor

- **email_mbmlbook/data.py**: create helper functions for parsing rows
- **email_mbmlbook/data.py**: remove features on construction
- **email_mbmlbook/data.py**: remove unused methods of FeatureSet
- **email_mbmlbook/data.py**: iterate over many users instead of expecting a single user
- **email_mbmlbook**: change self.base to the psudeo root of the file