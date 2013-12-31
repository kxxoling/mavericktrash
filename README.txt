macProTrash Icon - Jonathan Hirz - jonathanhirz.com
2013/12/18

Tested only on OS X Mavericks, and it works just fine. Backup your originals just in case.

Installation:
Navigate to Machintosh HD > System > Library > CoreServices > Dock
Right click and "Show Package Contents"
Contents > Resources
Scroll down to find the files "trashempty.png", "trashempty@2x.png", etc and back them up. There should be 8.
Replace old icons with new ones, and delete the reflections. They aren't needed.
Open Terminal.app and type "killall Dock".
Enjoy!
