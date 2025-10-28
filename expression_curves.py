import nuke

class Curves:
    def __init__(self, k, wavelength_str, offset_str, max_str, min_str):

        self.k = k
        self.wavelength_str = wavelength_str
        self.offset_str = offset_str
        self.max_str = max_str
        self.min_str = min_str

    def extract_params(self,k, wavelength_str, offset_str, max_str, min_str):

        parameter_list = []

        if wavelength_str.text() == '':
            param_wl = str(1)
        else:
            param_wl = wavelength_str.text()
        parameter_list.append(param_wl)

        if offset_str.text() == '':
            param_offset = str(0)
        else:
            param_offset = offset_str.text()
        parameter_list.append(param_offset)

        if max_str.text() == '':
            param_max = str(1)
        else:
            param_max = max_str.text()
        parameter_list.append(param_max)

        if min_str.text() == '':
            param_min = str(0)
        else:
            param_min = min_str.text()
        parameter_list.append(param_min)

        return parameter_list

    def compute_bounce_curve(self,k, wavelength_str, offset_str, max_str, min_str):

        selected_knob = k.currentText()
        act_knob = nuke.selectedNode().knob(selected_knob)

        parameter_list = self.extract_params(k, wavelength_str, offset_str, max_str, min_str)

        param_wl = parameter_list[0]
        param_offset = parameter_list[1]
        param_max = parameter_list[2]
        param_min = parameter_list[3]

        act_knob.setExpression(
            "abs(sin(pi*(frame+" + param_offset + ")/" + param_wl + "))*("
            + param_max + "- " + param_min + ")+ " + param_min
        )

