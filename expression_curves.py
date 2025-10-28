import nuke

class Curves:
    def __init__(self, k, wavelength_str, offset_str, max_str, min_str):

        self.k = k
        self.wavelength_str = wavelength_str
        self.offset_str = offset_str
        self.max_str = max_str
        self.min_str = min_str

        if wavelength_str.text() == '':
            self.wavelength_str = str(1)
        else:
            self.wavelength_str = wavelength_str.text()

        if offset_str.text() == '':
            self.offset_str = str(0)
        else:
            self.offset_str = offset_str.text()

        if max_str.text() == '':
            self.max_str = str(1)
        else:
            self.max_str = max_str.text()

        if min_str.text() == '':
            self.min_str = str(0)
        else:
            self.min_str = min_str.text()

    def bounce_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"abs(sin(pi*(frame+ {self.offset_str} )/ {self.wavelength_str} ))*("
                               f" {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def sawtooth_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"((frame+ {self.offset_str} )% {self.wavelength_str} )/ {self.wavelength_str}"
                               f" *( {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def triangle_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"(asin(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str}"
                               f" ))/pi+0.5) *( {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def random_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"((random(frame+ {self.offset_str} ))) *( {self.max_str}"
                               f" - {self.min_str} )+ {self.min_str}"
                               )

    def square_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"int(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str} )+1)/2 *( {self.max_str} - {self.min_str} )*2+ {self.min_str}")

    def sin_curve(self):

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        act_knob.setExpression(f"(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str} )+1)/2 *( {self.max_str} - {self.min_str} )+ {self.min_str}")