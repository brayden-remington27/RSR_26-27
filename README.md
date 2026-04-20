# RSR_26-27
A new repository for a new year. I'm going to try something new, easily adaptable, and centralized.

## OUTLINE
- A new document type, readable into code that easily interacts with an ROV focused codebase, EG:
  - easily setup display, inputs, outputs
  - add custom scripts
- App for easy setup of raspi to broadcast and create necessary daemons

---

## CODE

### Computer

#### main.rov
- This is the main file that has the setup of the code which gets compiled into actual code.
- 

#### compiler.py
- This compiles `.rov` files as runnable, creating objects and displaying based on what is in the passed file.
- 

---

### ROV Setup

#### setup.deb
- This is the app that sets up the ROV with all the right daemons and broadcasting
  - it sets up the:
    - pigpio daemon
    - mediamtx daemon
    - ffmpeg daemon
