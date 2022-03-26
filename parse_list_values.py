import itertools
from itertools import groupby
import more_itertools

features = [
    "FromMe",
    "ToCcPosition",
    "HasAttachments",
    "BodyLength",
    "SubjectLength",
    "SubjectPrefix",
    "Sender",
    "Recipient",
]
refs = [
    "ref1",
    "ref3",
    "ref10",
    "ref17",
    "ref30",
    "ref35",
    "ref49",
    "ref706",
    "ref1089",
]
doubles = ["0", "1", "0", "1", "1", "1", "1", "0.5", "0.5"]
res = [
    "FromMe",
    "ToCcPosition",
    "HasAttachments",
    "BodyLength",
    "SubjectLength",
    "SubjectPrefix",
    "Sender",
    "Recipient",
    "Recipient",
]

values = []
for element, group in groupby(res):
    group = list(group)
    if len(group) > 1:
        values.append(";".join(group))
    else:
        values.append(element)


# values = []
# list_like = []
# _feature = ""

# for feature, ref, double in itertools.zip_longest(features, refs, doubles):
#     if feature is None:
#         list_like.append((_feature, double))
#     values.append(ref)
#     _feature = ref

refs = [
    "ref1",
    "ref3",
    "ref10",
    "ref17",
    "ref30",
    "ref35",
    "ref49",
    "ref706",
    "ref1089",
    "ref1093",
]
doubles = ["0", "1", "0", "1", "1", "1", "1", "0.333", "0.333", "0.333"]

refs = [
    "ref1",
    "ref706",
    "ref1089",
    "ref3",
    "ref10",
    "ref17",
    "ref30",
    "ref35",
    "ref49",
]
doubles = [
    "0",
    "0.5",
    "0.5",
    "1",
    "0",
    "1",
    "1",
    "1",
    "1",
]

refs = [
    "ref1",
    "ref3",
    "ref10",
    "ref17",
    "ref30",
    "ref35",
    "ref49",
    "ref706",
    "ref1089",
    "ref1093",
]
doubles = ["0", "1", "0", "1", "1", "1", "1", "0.333", "0.333", "0.333"]

queue = []
it_f = more_itertools.peekable(features)
it_d = more_itertools.peekable(doubles)
for feature, ref, double in itertools.zip_longest(it_f, refs, it_d):
    if not (float(double) < 1 and float(double) > 0):
        print(feature, ref, double)
        continue

    if float(double) < 1 and float(double) > 0:
        if float(it_d.peek(1)) < 1 and float(it_d.peek(1)) > 0:
            it_f.prepend(feature)

    print(feature, ref, double)
