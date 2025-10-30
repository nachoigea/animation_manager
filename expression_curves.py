import nuke

class Curves:
    """
    A Class representing the expression curves that can be generated

    Attributes:
        k: knob selected to curve in
        wavelenth_str: wavelength of the curve
        offset_str: offset in the x axis the curve can have
        max_str: maximum value the curve can reach
        min_str: minimum value the curve can reach
    """

    def __init__(self, k, wavelength_str, offset_str, max_str, min_str):
        """Initialize the class

        :param k: knob selected to curve in
        :param wavelength_str: wavelength of the curve
        :param offset_str: offset in the x axis the curve can have
        :param max_str: maximum value the curve can reach
        :param min_str: minimum value the curve can reach
        """

        self.k = k
        self.wavelength_str = wavelength_str
        self.offset_str = offset_str
        self.max_str = max_str
        self.min_str = min_str

    def update_expression_values(self, wavelength_str, offset_str, max_str, min_str):
        """Update the expression curve values depending on the panel values

        :param wavelength_str: wavelength of the curve
        :param offset_str: offset in the x-axis the curve can have
        :param max_str: maximum value the curve can reach
        :param min_str: minimum value the curve can reach

        """

        self.wavelength_str = wavelength_str.text()
        self.offset_str = offset_str.text()
        self.max_str = max_str.text()
        self.min_str = min_str.text()

    def bounce_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression bounce curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"abs(sin(pi*(frame+ {self.offset_str} )/ {self.wavelength_str} ))*("
                               f" {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def sawtooth_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression sawtooth curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"((frame+ {self.offset_str} )% {self.wavelength_str} )/ {self.wavelength_str}"
                               f" *( {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def triangle_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression triangle curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"(asin(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str}"
                               f" ))/pi+0.5) *( {self.max_str} - {self.min_str} )+ {self.min_str}"
                               )

    def random_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression random curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"((random(frame+ {self.offset_str} ))) *( {self.max_str}"
                               f" - {self.min_str} )+ {self.min_str}"
                               )

    def square_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression square curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"int(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str} )+1)/2 *( {self.max_str} - {self.min_str} )*2+ {self.min_str}")

    def sin_curve(self, wavelength_str, offset_str, max_str, min_str):
        """Generate the expression sin curve
        """

        selected_knob = self.k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        self.update_expression_values(wavelength_str, offset_str, max_str, min_str)

        act_knob.setExpression(f"(sin(2*pi*(frame+ {self.offset_str} )/ {self.wavelength_str} )+1)/2 *( {self.max_str} - {self.min_str} )+ {self.min_str}")