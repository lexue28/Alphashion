def selectImageandAnalyze():
    #can analyze in here
    from tkinter import filedialog as fd
    filename = fd.askopenfilename()
    print(filename)


    import shutil
    shutil.copy(filename, "capture.png")
'''
def selectImageandAnalyze():
    from analysis import analyze
    from tkinter import filedialog as fd
    filename = fd.askopenfilename()
    print(filename)


    import shutil
    shutil.copy(filename, "capture.png")

    analyze()
'''
