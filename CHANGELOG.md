## Unreleased

### Refactor

- **initial.py-offline.py-parse_list_values.py-personalisation.py-seed.py-separate.py-with_recipient.py-with_subject_prefix.py**: remove first iterations

### Fix

- **README**: chage file extension of README

## 0.3.0 (2022-03-26)

### Feat

- **email_mbmlbook/__init__.py-email_mbmlbook/source.py**: add constant for which files to parse from the github repo
- **get_data.py**: add entry point for the project
- **data/-data/*.csv**: add parsed data
- **with_subject_prefix.py**: first iteration of parsing WithSubjectPrefixInputs.objml
- **with_recipient.py**: first iteration parsing WithRecipientInputs.objml
- **separate.py**: first iteration parsing SeparateInputs.objml
- **seed.py**: first iteration of parsing Seed[1|2]Inputs.objml
- **personalisation.py**: first iteration of parsing Personalisation[1|2]Inputs.objml
- **parse_list_values.py**: first iteration of parsing list values within objml file
- **offline.py**: first iteratoin of parsing OfflineInputs.objml
- **CHANGELOG.md**: create change log

### Fix

- **seed.py**: fix copy paste error

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
