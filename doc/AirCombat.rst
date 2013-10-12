
Air Combat IV script by JulioNIB v1.4

With colaboration (testing/jet models/tips/code tips) of:

core.max2010 - https://www.youtube.com/user/coremax2010
metalwars - https://www.youtube.com/user/Metalwarz
SkylineGTRFreak - https://www.youtube.com/user/SkylineGTRR34Freak
zzcool (taltigolt) - https://www.youtube.com/user/taltigolt
Hardsty1e - http://www.gtagaming.com/forums/member.php?u=107738
Fredwalktrought - https://www.youtube.com/user/fredwalkthrough



This script will add (or at least try) jet sound, cannons, rockets/missiles, bombs, flares, 
wings/flaps/gears movement and high speed to the jets in GTA iV, TBoGT and TLaD


Installation
-------------

* Copy all files from this zip to your gtaiv.exe folder, backup old files before overwriting
* Copy the correct scripthook.dll file from the folder that indicates your patch version
* Download and install one jet model (you will find download links inside the subfolders of the Custom jets folder)
* Inside the folder Jets you will have an default list of jets (.ini files), each jet installed must have one file, 
  you can copy and edit one jet_ .INI file to customize an new jet, the most important variable its "jet_model",
  it contains the name of the model of the jet
* Follow the instructions in the HANDLING.txt file to make the new model fly


in the jet_ .ini file we can customize:
======================================

* name of tag jet model
* display name (for spawn menu)
* console command for spawn
* 16 rockets/bombs (and they explosion size and force)
* 4 engines
* 4 cannons
* 3 extra cameras (script has more 2 default: cockpit and "nose" camera)
* some sounds
* flaps/wings/gears movement (doors/trunks/hoods)
etc.

in general .ini file (AC-IV.ini):
==================================

* aim ease (increase to make easier to lock rockets on enemies)
* Nenemy evade difficult
* hotkeys
* space trip
* etc.



each jet_xxxxx.ini file inside Jets folder has config for that desired model, you just need to install the model and change the
variable jet_model to the name of the installed model



the HANDLING should be the handling of planes, not the VTOL style, look at the file handling.txt to see
how to configure the game to able the jet models to fly


The DEFAULT HOTKEYS are:
=======================

To control the jet:

* W (accel.)
* S (desaccel.)
* A (or numpad 4)
* D (or numpad 6)
* Shift (or numpad 8)
* Control (or numpad 5)
* numpad 7 - turn left
* numpad 9 - turn right

* X - Switch cam
* Right click - Follow missile/bomb with camera
* Space shoot missiles
* Numpad0 - Shoot cannon
* Q - Drop bomb
* E - Release flare to avoid missiles (hold to release one by one)
* F - Enter Jet / Exit Jet / Eject (if flying)
* Left/Right help "drive" the jet while in the ground
* 0 - Spawn menu
* Enter - Spawn select Jet in spawn menu, hold shift to spawn and start flying
* 2 - Spawn enemy
* 3 - Spawn fugitive

when on ground:
==============
* Left/Right (or numpads 7/9) - turn left or right
* S - Break


if the jet SPIN/ROLL too much when using numpads, reduce the value of the variables:


* moveLeftForce=1
* moveRightForce=1
* rollLeftForce=1
* rollRightForce=1
* moveUpForce=1
* moveDownForce=1


to something like 0.3, in the jet_xxxx.ini file (folder Jets)


if the scripts CRASH when the game starts, use the console command reloadscripts :)
this have more chances to happen in TLaD

