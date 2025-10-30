#-------------------------------------------------------------------------------
#Animation Manager by Nacho Igea
# Complete python sript editor for Nuke
#-------------------------------------------------------------------------------

import nuke
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets

from nukescripts.panels import registerWidgetAsPanel

import expression_curves
import utils
import modify_curves

class AnimationManager(QtWidgets.QWidget):
    """A Class representing the Animation Manager panel
    """

    def __init__(self, parent=None):
        """Initialize the Animation Manager

        :param parent:
        """
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        #creation of the tabs
        self.tab = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()

        #custom curve tab
        #creation of the graphic elements
        self.combo = QtWidgets.QComboBox()
        self.combo.setFixedWidth(150)

        #knob group
        self.label = QtWidgets.QLabel("Knob")
        self.group1 = QtWidgets.QGroupBox("Select animated knob")
        self.refresh_button = QtWidgets.QPushButton("Update node")

        #frame range group
        self.group2 = QtWidgets.QGroupBox("New frame range")
        self.my_first_frame = QtWidgets.QLineEdit()
        self.my_first_frame.setAlignment(QtCore.Qt.AlignLeft)
        self.my_first_frame.setFixedWidth(50)
        self.my_last_frame = QtWidgets.QLineEdit()
        self.my_last_frame.setFixedWidth(50)
        self.label_my_first_frame = QtWidgets.QLabel("First frame")
        self.label_my_first_frame.setIndent(1)
        self.label_my_last_frame = QtWidgets.QLabel("Last frame")

        #offset group
        self.offset_group = QtWidgets.QGroupBox("Keyframes offset")
        self.offset_label = QtWidgets.QLabel("Offset")
        self.offset_value = QtWidgets.QLineEdit()
        self.offset_value.setFixedWidth(50)

        #multiply group
        self.mult_group = QtWidgets.QGroupBox("Keyframes multiply")
        self.mult_label = QtWidgets.QLabel("Multiply")
        self.mult_value = QtWidgets.QLineEdit()
        self.mult_value.setFixedWidth(50)

        #loop group
        self.loop_group = QtWidgets.QGroupBox("")
        self.loop_group_offset = QtWidgets.QGroupBox("")
        self.loop_group2 = QtWidgets.QGroupBox("Loop Animation")
        self.loop_button = QtWidgets.QPushButton("Loop Animation")
        self.loop_slider = QtWidgets.QLineEdit()
        self.loop_slider = QtWidgets.QLineEdit()
        self.loop_slider.setFixedWidth(50)
        self.loop_slider_label = QtWidgets.QLabel("Offset Animation")
        self.loop_slider_label.setIndent(1)
        self.loop_my_first_frame = QtWidgets.QLineEdit()
        self.loop_my_first_frame.setAlignment(QtCore.Qt.AlignLeft)
        self.loop_my_first_frame.setFixedWidth(50)
        self.loop_my_last_frame = QtWidgets.QLineEdit()
        self.loop_my_last_frame.setFixedWidth(50)
        self.loop_label_my_first_frame = QtWidgets.QLabel("Offset Loop First frame")
        self.loop_label_my_first_frame.setIndent(1)
        self.loop_label_my_last_frame = QtWidgets.QLabel("Offset Loop Last frame")

        #creation of layouts
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout1.setAlignment(QtCore.Qt.AlignTop)
        self.in_layout = QtWidgets.QHBoxLayout()
        self.frame_range_layout = QtWidgets.QHBoxLayout()
        self.frame_range_layout.addStretch(2)
        self.frame_range_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.offset_layout = QtWidgets.QHBoxLayout()
        self.mult_layout = QtWidgets.QHBoxLayout()
        self.loop_layout = QtWidgets.QHBoxLayout()
        self.loop_offset_layout = QtWidgets.QHBoxLayout()
        self.loop_offset_layout.addStretch(2)
        self.loop_offset_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.loop_frame_range_layout = QtWidgets.QHBoxLayout()
        self.loop_frame_range_layout.addStretch(2)
        self.loop_frame_range_layout.setAlignment(QtCore.Qt.AlignLeft)

        #adding groups to layouts
        self.layout1.addWidget(self.group1)
        self.layout1.addWidget(self.group2)
        self.layout1.addWidget(self.offset_group)
        self.layout1.addWidget(self.mult_group)
        self.layout1.addWidget(self.loop_group2)
        self.layout1.addWidget(self.loop_group)
        self.layout1.addWidget(self.loop_group_offset)

        #adding graphic elements to layouts
        self.in_layout.addWidget(self.label)
        self.in_layout.addWidget(self.combo)
        self.in_layout.addWidget(self.refresh_button)
        self.group1.setLayout(self.in_layout)

        self.loop_offset_layout.addWidget(self.loop_slider_label)
        self.loop_offset_layout.addWidget(self.loop_slider)
        self.loop_group_offset.setLayout(self.loop_offset_layout)

        self.loop_frame_range_layout.addWidget(self.loop_label_my_first_frame)
        self.loop_frame_range_layout.addWidget(self.loop_my_first_frame)
        self.loop_frame_range_layout.addWidget(self.loop_label_my_last_frame)
        self.loop_frame_range_layout.addWidget(self.loop_my_last_frame)
        self.loop_group.setLayout(self.loop_frame_range_layout)

        self.frame_range_layout.addWidget(self.label_my_first_frame)
        self.frame_range_layout.addWidget(self.my_first_frame)
        self.frame_range_layout.addWidget(self.label_my_last_frame)
        self.frame_range_layout.addWidget(self.my_last_frame)
        self.group2.setLayout(self.frame_range_layout)

        self.offset_layout.addWidget(self.offset_label)
        self.offset_layout.addWidget(self.offset_value)
        self.offset_group.setLayout(self.offset_layout)

        self.mult_layout.addWidget(self.mult_label)
        self.mult_layout.addWidget(self.mult_value)
        self.mult_layout.addWidget(self.loop_button)
        self.mult_group.setLayout(self.mult_layout)

        self.loop_layout.addWidget(self.loop_button)

        self.loop_group2.setLayout(self.loop_layout)

         #adding tab to layout
        self.tab1.setLayout(self.layout1)
        self.tab2 = QtWidgets.QWidget()

        #expression curve tab
        #creation of the graphic elements
        self.combo_curve = QtWidgets.QComboBox()
        self.combo_curve.setFixedWidth(150)
        self.label_curve = QtWidgets.QLabel("Knob")
        self.group1_curve = QtWidgets.QGroupBox("Select knob to animate")

        self.group2_curve = QtWidgets.QGroupBox("Set parameters")
        self.wavelength_label = QtWidgets.QLabel("Wavelength")
        self.wavelength_value = QtWidgets.QLineEdit()
        self.wavelength_value.setFixedWidth(50)

        self.group_offset_curve = QtWidgets.QGroupBox()
        self.offset_label_curve = QtWidgets.QLabel("Frame Offset")
        self.offset_valueCurve = QtWidgets.QLineEdit()
        self.offset_valueCurve.setFixedWidth(50)

        self.group_height = QtWidgets.QGroupBox()
        self.my_first_frameCurve = QtWidgets.QLineEdit()
        self.my_first_frameCurve.setFixedWidth(50)
        self.my_last_frameCurve = QtWidgets.QLineEdit()
        self.my_last_frameCurve.setFixedWidth(50)
        self.label_my_first_frameCurve = QtWidgets.QLabel("Minimum value")
        self.label_my_first_frameCurve.setIndent(1)
        self.label_my_last_frameCurve = QtWidgets.QLabel("Maximum value")

        #creation of buttons
        self.group_buttons = QtWidgets.QGroupBox("Generate the curve")
        self.random_button = QtWidgets.QPushButton("Random")
        self.triangle_button = QtWidgets.QPushButton("Triangle")
        self.sine_button = QtWidgets.QPushButton("Sine")
        self.square_button = QtWidgets.QPushButton("Square")
        self.sawtooth_button = QtWidgets.QPushButton("Sawtooth")
        self.bounce_button = QtWidgets.QPushButton("Bounce")

        #creation of layouts
        self.in_layout_curve = QtWidgets.QHBoxLayout()
        self.in_layout_curve.addWidget(self.label_curve)
        self.in_layout_curve.addWidget(self.combo_curve)
        self.group1_curve.setLayout(self.in_layout_curve)
        self.in_layout_curve.setAlignment(QtCore.Qt.AlignTop)

        #adding graphic elements to layouts
        self.wavelength_layout = QtWidgets.QHBoxLayout()
        self.wavelength_layout.addWidget(self.wavelength_label)
        self.wavelength_layout.addWidget(self.wavelength_value)

        self.offset_curve_layout = QtWidgets.QHBoxLayout()
        self.offset_curve_layout.addWidget(self.offset_label_curve)
        self.offset_curve_layout.addWidget(self.offset_valueCurve)

        self.height_curve_layout = QtWidgets.QHBoxLayout()
        self.height_curve_layout.addWidget(self.label_my_first_frameCurve)
        self.height_curve_layout.addWidget(self.my_first_frameCurve)
        self.height_curve_layout.addWidget(self.label_my_last_frameCurve)
        self.height_curve_layout.addWidget(self.my_last_frameCurve)

        self.buttons_layout = QtWidgets.QGridLayout()
        self.buttons_layout.addWidget(self.random_button, 0,0)
        self.buttons_layout.addWidget(self.triangle_button, 0,1)
        self.buttons_layout.addWidget(self.sine_button,0,2)
        self.buttons_layout.addWidget(self.square_button,1,0)
        self.buttons_layout.addWidget(self.sawtooth_button,1,1)
        self.buttons_layout.addWidget(self.bounce_button,1,2)

        self.group2_curve.setLayout(self.wavelength_layout)
        self.group_offset_curve.setLayout(self.offset_curve_layout)
        self.group_height.setLayout(self.height_curve_layout)
        self.group_buttons.setLayout(self.buttons_layout)

        #getting the animated knobs of the selected node
        try:
            knob_list = utils.get_anim_knobs()
            self.combo.addItems(knob_list)

            current_node_name = nuke.selectedNode().name()
        except ValueError:
            nuke.message("Please select a node")

        #adding groups to layouts
        self.layout2 = QtWidgets.QVBoxLayout()
        self.layout2.addWidget(self.group1_curve)

        self.layout2.addWidget(self.group2_curve)
        self.layout2.addWidget(self.group_offset_curve)
        self.layout2.addWidget(self.group_height)
        self.layout2.addWidget(self.group_buttons)

        self.layout2.addStretch(2)
        self.tab2.setLayout(self.layout2)

        #adding tabs to master layout
        self.tab.addTab(self.tab1, "Adapt custom curve")
        self.tab.addTab(self.tab2, "Curve presets")

        self.current_node_label = QtWidgets.QLabel(current_node_name)
        self.current_node_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_node_label.setStyleSheet("color: rgb(223, 202, 98); font: bold 28px")
        self.space_label = QtWidgets.QLabel(" ")
        self.space_label2 = QtWidgets.QLabel(" ")
        self.tabs_label = QtWidgets.QLabel("Generate or modify your animation curves")
        self.sign_label = QtWidgets.QLabel("by Nacho Igea")

        self.master_layout = QtWidgets.QVBoxLayout()
        self.master_layout.addWidget(self.current_node_label)
        self.master_layout.addWidget(self.space_label)
        self.master_layout.addWidget(self.refresh_button)
        self.master_layout.addWidget(self.space_label2)
        self.master_layout.addWidget(self.tabs_label)
        self.master_layout.addWidget(self.space_label2)
        self.master_layout.addWidget(self.tab)
        self.master_layout.addWidget(self.space_label2)
        self.master_layout.addWidget(self.sign_label)

        #getting all the knobs in the selected node
        all_knob_list = utils.get_all_knobs()
        self.combo_curve.addItems(all_knob_list)

        #setting values for the inputs
        is_anim = utils.check_animation()
        if is_anim:

            first_frame = utils.get_first_frame(self.combo)
            self.my_first_frame.setText(str(first_frame))

            last_frame = utils.get_last_frame(self.combo)
            self.my_last_frame.setText(str(last_frame))

        self.offset_value.setText(str(0))
        self.mult_value.setText(str(1))

        self.loop_my_first_frame.setText(str(0))
        self.loop_my_last_frame.setText(str(0))
        self.loop_slider.setText(str(0))

        self.wavelength_value.setText(str(10))
        self.offset_valueCurve.setText(str(0))
        self.my_first_frameCurve.setText(str(0))
        self.my_last_frameCurve.setText(str(1))

        #adding functions to text boxes in custom curves tab
        self.offset_value.returnPressed.connect(lambda : modify_curves.add_offset_edit(self.combo, self.offset_value))
        self.mult_value.returnPressed.connect(lambda : modify_curves.multiply_edit(self.combo, self.mult_value))
        self.my_first_frame.returnPressed.connect(lambda : modify_curves.adapt_anim_first_frame(self.my_first_frame, self.combo))
        self.my_last_frame.returnPressed.connect(lambda : modify_curves.adapt_anim_last_frame(self.my_last_frame, self.combo))

        self.loop_slider.returnPressed.connect(lambda : modify_curves.offset_anim(
            self.combo, self.loop_slider, self.loop_my_last_frame, self.loop_my_first_frame
        ))
        self.loop_my_first_frame.returnPressed.connect(lambda : modify_curves.offset_anim(
            self.combo, self.loop_slider, self.loop_my_last_frame, self.loop_my_first_frame
        ))
        self.loop_my_last_frame.returnPressed.connect(lambda : modify_curves.offset_anim(
            self.combo, self.loop_slider, self.loop_my_last_frame, self.loop_my_first_frame
        ))

        #adding functions to push buttons in expression curve tab
        preset_curves= expression_curves.Curves(
            self.combo_curve, self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        )
        self.random_button.clicked.connect(lambda : preset_curves.random_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))
        self.triangle_button.clicked.connect(lambda : preset_curves.triangle_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))
        self.sine_button.clicked.connect(lambda : preset_curves.sin_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))
        self.square_button.clicked.connect(lambda : preset_curves.square_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))
        self.sawtooth_button.clicked.connect(lambda : preset_curves.sawtooth_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))
        self.bounce_button.clicked.connect(lambda: preset_curves.bounce_curve(
            self.wavelength_value, self.offset_valueCurve, self.my_last_frameCurve, self.my_first_frameCurve
        ))

        #addinf functions to buttons and pulldown in custom curve tab
        self.loop_button.clicked.connect(lambda : modify_curves.loop_anim(self.combo))
        self.refresh_button.clicked.connect(lambda : self.refresh_function())
        self.combo.currentTextChanged.connect(lambda : self.refresh_knob(self.combo))

        self.setLayout(self.master_layout)
        self.setGeometry(30, 30, 30, 15)

        self.refresh_knob(self.combo)


    def refresh_function(self):
        """Update the panel when a different node is selected from the original

        """
        # reuse existing logic to get knobs of current selected node.
        self.combo.clear()
        self.combo.addItems(utils.get_anim_knobs())

        is_anim = utils.check_animation()

        self.my_first_frame.clear()
        self.my_last_frame.clear()

        if is_anim:

            first_frame = utils.get_first_frame(self.combo)
            self.my_first_frame.setText(str(first_frame))

            last_frame = utils.get_last_frame(self.combo)
            self.my_last_frame.setText(str(last_frame))

        self.combo_curve.clear()
        self.combo_curve.addItems(utils.get_all_knobs())

        self.current_node_label.clear()
        self.current_node_label.setText(nuke.selectedNode().name())

    def refresh_knob(self, k):
        """Hide the parameters in the custom curve tab if the knob selected in the pulldown has an expression
            and shows them if it doesn't

        :param k: knob to perform the action
        """

        is_anim = utils.check_animation()

        self.my_first_frame.clear()
        self.my_last_frame.clear()

        sel_knob = k.currentText()
        act_knob = nuke.selectedNode().knob(sel_knob)

        is_string = utils.find_string_curve(act_knob, 'curve')

        if is_anim:
            if not act_knob.hasExpression():

                first_frame = utils.get_first_frame(self.combo)
                self.my_first_frame.setText(str(first_frame))

                last_frame = utils.get_last_frame(self.combo)
                self.my_last_frame.setText(str(last_frame))

            elif act_knob.hasExpression() == True and is_string == 1:

                first_frame = utils.get_first_frame(self.combo)
                self.my_first_frame.setText(str(first_frame))

                last_frame = utils.get_last_frame(self.combo)
                self.my_last_frame.setText(str(last_frame))

        if act_knob.hasExpression() == True and is_string == 0:

            self.group2.hide()
            self.offset_group.hide()
            self.mult_group.hide()
            self.loop_group.hide()
            self.loop_group_offset.hide()
            self.loop_group2.hide()
        elif act_knob.hasExpression() == True and is_string == 1:

            self.group2.show()
            self.offset_group.show()
            self.mult_group.show()
            self.loop_group.show()
            self.loop_group_offset.show()
            self.loop_group2.show()
        elif not act_knob.hasExpression():

            self.group2.show()
            self.offset_group.show()
            self.mult_group.show()
            self.loop_group.show()
            self.loop_group_offset.show()
            self.loop_group2.show()

registerWidgetAsPanel('main.AnimationManager', 'Animation Manager', 'animation_manager.id')
#nuke.menu( 'Nuke' ).addCommand('Animation Manager', lambda: AnimationManager().show())