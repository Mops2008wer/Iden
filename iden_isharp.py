from ram import _read
from ram import _mov
from ram import _read_metadata
from ram import _mov_metadata


def def_create(metadata):
    _mov("temp_build.def", metadata)

def def_build(file, metadata_file):
    data = _read("temp_build.def")
    _mov(file, data)
    metadata = _read(metadata_file)
    metalist = metadata.split("-")
    metalist.append(file)
    _mov(metadata_file, "-".join(metalist))
    print(file + " build successfully!")
    return len(metalist) - 1

def metadata_create():
    _mov("temp_build.metadata", "")

def metadata_add(data):
    metadata = _read("temp_build.metadata")
    metalist = metadata.split("-")
    metalist.append(data)
    _mov("temp_build.metadata", "-".join(metalist))
    return len(metalist) - 1

def metadata_build(file):
    data = _read("temp_build.metadata")
    _mov(file, data)
    print(file + " build successfully!")
    return file

def i_print(md1, md3, md2, bloean, style, icon):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("print_ui=" + str(md1) + "=" + str(md2) + "=" + str(bloean) + "=" + str(style) + "=" + str(icon) + "=" + str(md3))
    _mov("temp_build.def", ";
".join(metalist))
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("print_ui_2=" + str(md1) + "=" + str(md2) + "=" + str(md3) + "=" + str(bloean) + "=" + str(style) + "=" + str(icon))
    _mov("temp_build.def", ";
".join(metalist))

def i_input(md1, md2, save, style, bloean, icon):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("input_ui=" + str(md1) + "=" + str(md2) + "=" + str(save) + "=" + str(style) + "=" + str(bloean) + "=" + str(icon))
    _mov("temp_build.def", ";
".join(metalist))

def i_run(md1):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("run=_md=" + str(md1))
    _mov("temp_build.def", ";
".join(metalist))

def i_int(type, md1, md2, save):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("intopr=" + str(type) + "=" + str(md1) + "=" + str(md2) + "=" + str(save))
    _mov("temp_build.def", ";
".join(metalist))

def i_ifelse(type, md1, md2_text, func1, func2):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("true_false=" + str(type) + "=" + str(md1) + "=" + str(md2_text) + "=" + str(func1) + "=" + str(func2))
    _mov("temp_build.def", ";
".join(metalist))

def i_code(code):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append(code)
    _mov("temp_build.def", ";
".join(metalist))

def i_file(type, file, md):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("metadata=" + type + "=" + str(file) + "=" + str(md))
    _mov("temp_build.def", ";
".join(metalist))

def i_exit():
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("exit_app")
    _mov("temp_build.def", ";
".join(metalist))

def i_meta(data, md):
    metadata = _read("temp_build.def")
    metalist = metadata.split(";
")
    metalist.append("metadata=" + str(data) + "=" + str(md))
    _mov("temp_build.def", ";
".join(metalist))

def i_build(name, app_files, app_libs, build):
    app_build = ""
    for app_file in app_files:
        file = open(("apps/" + app_file), "r")
        data = file.read()
        file.close()
        app_build = app_build + """
file = open(('apps/' + '""" + app_file + """'), "w")
file.write( + str(data) + )
file.close()
print('File: """ + app_file + """ installed!')"""
    for app_lib in app_libs:
        file = open((app_lib), "r")
        data = file.read()
        file.close()
        app_build = app_build + """
file = open(('""" + app_lib + """'), "w")
file.write( + str(data) + )
file.close()
print('Lib: """ + app_lib + """ installed!')"""
    app_build = app_build + """
input('""" + name + """ installed!')
"""
    file = open((name + "_build" + str(build) + ".py"), "w")
    file.write(app_build)
    file.close()
    print("Installer build!")

