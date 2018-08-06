# PyQt-GUI-UI-to-PY-to-EXE
<b>This app is created in Python</b>
<h2>How to use this?</h2>
<ul>
<li>Make sure PyQt4 is properly installed. Use pip freeze to list the installed packages</li>
<li>Install PyInstaller: pip install pyinstaller</li>
<li>Run the app: open the main.py and run it using your IDE or simply open EasyConverter.exe</li>
<li>Test by converting a convertMe.ui file to .py file</li>
<li>Take a note as double clicking your generated .py file won't work right away:<ol>
  <li>Open the main.py for editing and look for the main class.</li>
  <li>First import sys
  <li>In the class brackets, replace anything present with QtGui.QWidget</li>
  <li>Then within this class make a initial/constructor method: def __init__(self):</li>
  <li>Within constructor add these two lines: QtGui.QWidget.__init__(self) and self.setupUi(self)</li>
  </ol></li>
<li>Everything's done. Now run by double clicking your .py file</li>
</ul>

<b>NOTE</b>
<p>I have created the EasyConverter.exe app by using my python code onto itself. main.py is the main python script that does all this conversion. I simply created its exe using itself for my easy. You can use it as well.</p>
<b>Remember</b> if EasyConverter.exe doesn't run, you can double click the main.py and use it for your conversion.</p>
<p>On Linux and Mac, you have to use main.py as .exe won't work there!</p>
