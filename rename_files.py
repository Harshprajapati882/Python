import os

renames = [
    ("Python_Learning/027-Arrays/Arrays.py", "Python_Learning/027-Arrays/arrays.py"),
    ("Python_Learning/003-Data-Structures/DS.py", "Python_Learning/003-Data-Structures/data_structures.py"),
    ("Python_Learning/017-Dictionaries/Dics.py", "Python_Learning/017-Dictionaries/dictionaries.py"),
    ("Python_Learning/015-Sets/Set.py", "Python_Learning/015-Sets/sets.py"),
    ("Python_Learning/014-Tuples/Tuple.py", "Python_Learning/014-Tuples/tuples.py"),
    ("Python_Learning/012-List/List.py", "Python_Learning/012-List/list.py"),
    ("Python_Learning/001-Getting-Started/Python_Intro.py", "Python_Learning/001-Getting-Started/python_intro.py"),
    ("Python_Learning/002-Modules-and-Packages/Pips&Modules.py", "Python_Learning/002-Modules-and-Packages/pips_and_modules.py"),
    ("Python_Learning/004-Basic-Syntax/All.py", "Python_Learning/004-Basic-Syntax/basic_syntax.py"),
    ("Python_Learning/005-Input-and-Output/Typecasting.py", "Python_Learning/005-Input-and-Output/typecasting.py"),
    ("Python_Learning/006-Control-Flow-If-Else/if-else.py", "Python_Learning/006-Control-Flow-If-Else/if_else.py"),
    ("Python_Learning/007-Control-Flow-Loops/Loops.py", "Python_Learning/007-Control-Flow-Loops/loops.py"),
    ("Python_Learning/009-Conti&Break/Conti&Br.py", "Python_Learning/009-Conti&Break/continue_and_break.py"),
    ("Python_Learning/010-TRY_Except/TryExcept.py", "Python_Learning/010-TRY_Except/try_except.py"),
    ("Python_Learning/011-Operator/OP.py", "Python_Learning/011-Operator/operator.py"),
    ("Python_Learning/016-Match/Match.py", "Python_Learning/016-Match/match.py"),
    ("Python_Learning/018-Date/Date.py", "Python_Learning/018-Date/date.py"),
    ("Python_Learning/019-Modules/Module.py", "Python_Learning/019-Modules/modules.py"),
    ("Python_Learning/020-Pass/Pass.py", "Python_Learning/020-Pass/pass_statement.py"),
    ("Python_Learning/021-Numbers/Number.py", "Python_Learning/021-Numbers/numbers.py"),
    ("Python_Learning/022-Control_Statement/Control_statement.py", "Python_Learning/022-Control_Statement/control_statement.py"),
    ("Python_Learning/023-String/String.py", "Python_Learning/023-String/string.py"),
    ("Python_Learning/024-String_Methods/String_Methods.py", "Python_Learning/024-String_Methods/string_methods.py"),
    ("Python_Learning/025-Function/Function_&_Function_types.py", "Python_Learning/025-Function/function_and_function_types.py"),
    ("Python_Learning/026-RegEx/RegEx.py", "Python_Learning/026-RegEx/regex.py"),
    ("Python_Learning/028-Function_Argument/D_Aug.py", "Python_Learning/028-Function_Argument/function_argument.py"),
]

for old_name, new_name in renames:
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found: {old_name}")
