array0 = {
    "String1":            ["String8",      True],
    "String2":              ["String8",      True],
    "String3":   ["String8",      True],
    "String4":                ["String8",      True],
    "String5":              ["String8",      True],
    "String6":       ["String8",      True],
    "String7":       ["String9",     True],
    "String8":       ["String13",            False],
    "String9":      ["String13",            False],
    "String10": 		["String14",      False],
    "String11":       ["String15", False]
}
array1 = ["String1", "String2", "String3", "String4", "String5", "String6", "String7", "String8", "String9", "String10", "String11", "String12", "String13", "String14", "String15", "String16", "String17"]
array2 = [x.name for x in discordmemberobject.roles]
array3 = [x.name for x in ctx.author.roles]
if any(x in array2 for x in list(array0)):
  array4 = [x for x in array2 if x in array1]
  array5 = [x for x in array3 if x in array1]
  if array1.index(array0[array4[-1]][0]) <= array1.index(rank) and array1.index(array0[array4[-1]][0]) <= array1.index(array5[-1]):
    #...
    return
