def copy_style():
    print("Copying style...")
    import os
    import matplotlib as mpl

    from pkg_resources import resource_string

    files = [
        "styles/oldplotlib.mplstyle",
    ]

    for fname in files:
        styles_path = os.path.join(mpl.get_data_path(), 'stylelib')
        path = os.path.join(styles_path, fname.split("/")[-1])
        text = resource_string(__name__, fname).decode()
        open(path, "w").write(text)
    print("Done!")