# Video Converter #

**Video Converter** is a Python GUI application (using wxPython) designed to use the HandBrake CLI application to batch convert video files.

## Development Requirements ##
Cross-development using [Aptana Studio 3](http://www.aptana.com/) started on 32-bit Python 2.6.1 on both Mac OS X 10.6.6 and Windows 7 64-bit using wxPython 2.8.9 32-bit.

Current requirements:

- [Python](http://www.python.org/download/) v2.7.3
- [wxPython](http://wxpython.org/) v2.8.12.1 32-bit
- [wxFormBuilder](http://wxformbuilder.org/) v3.1.70
- [HandBrake CLI](http://handbrake.fr/downloads2.php) v0.9.6
- [VoidSpace ConfigObj](http://www.voidspace.org.uk/python/configobj.html) v4 (included)

This has not been test on a Linux distribution.

## How to Use ##
It's a pretty simple, straight-forward application, but here are a few tips to help make things clear (hopefully).

### Preferences ###
The **Preferences Dialog** allows you to store the HandBrake CLI location, the HandBrake options, and the default source and destination folders.  The application will scan the source folder and all subfolders, so keep that in mind when setting this default.

### Running the Application ###
Once one or more video files are found, select at least one and click Process.  The application will capture the output from the HandBrake CLI process and dump it to the textbox.

## Future Plans, Roadmap ##
None at this time &mdash; other than hoping to learn from better Python programmers than myself.