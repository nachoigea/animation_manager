# Animation Manager
Panel that allows the artist to modify existing animations in any knob and creates expression curves without having to add the expression formula by hand.

It is mandatory to have a selected node in order to launch the panel, once it is launched you can change between nodes by pressing the update button

This panel has to modes:
- Modify Curves: the default one, works with animation curves made by hand. It allows the user to adapt the frame range of the curve, maintaining the "shape" and computing again each keyframe to keep consistency. It is also capable of multiplying and adding the values of the curve.

<img width="596" height="664" alt="animation_manager_modify_curves" src="https://github.com/user-attachments/assets/b2469118-12a8-47dd-959f-dba8892d3df4" />

- Curve presets: works with expression curves that can be added to any knob in the working node. It only needs to select which knob needs to be changed, then selecting the parameters of the expression and the type of curve the user wants. By pressing the curve button, the expression is automatically generated.

<img width="594" height="584" alt="animation_manager_curve_presets" src="https://github.com/user-attachments/assets/5f9818d4-d6b4-4564-aef2-a700d3a763e4" />


## Installation

To install it download ZIP and place the `AM_scripts` folder in your .nuke folder. Then add the following lines.

### To your menu.py

`import main`

### To your init.py

`nuke.pluginAddPath('./AM_scripts')`
