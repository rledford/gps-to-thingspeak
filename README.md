<h4>serial-to-thingspeak</h4>
<div>
    Works with Python 2.x and 3.x
</div>
<br>
<div>
    This is a configurable console application that reads a serial port for various GPS strings and updates a ThingSpeak channel with the latitude and longitude.
</div>
<br>
<div>
    The application will automatically start with the last used configuration. If no configuration file is found, a default one is generated.
    The default configuration is not suitable for all operating systems and has ThingSpeak options set to <code>null</code>.
</div>
<br>
<div>
    While the application is running press <code>Ctrl-C</code> to stop the run process and show the main menu.
</div>
<div>
    <h5>PyInstaller</h5>
    <div>
        Build executables with pyInstaller by using the following command <code>pyinstaller -F main.py -n name-of-executable-file</code>
    </div>
    <div>
        If building for Python 2.x, add the following to the pyinstaller command line options <code>--hidden-import=Queue</code>
    </div>
    <div>
        If building for python 3.x, add the following to the pyinstaller command line options <code>--hidden-import=queue</code>
    </div>
</div>
<div>
    <h5>Dependencies</h5>
    <ul>
        <li><a target='_blank' href='http://pyserial.readthedocs.io/en/latest/pyserial.html'>PySerial</a></li>
        <li><a target='_blank' href='http://docs.python-requests.org/en/master/'>requests</a></li>
    </ul>
</div>
