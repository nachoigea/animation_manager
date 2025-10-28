#-------------------------------------------------------------------------------
#Animation Manager by Nacho Igea
# Complete python sript editor for Nuke
#2021-2022
#-------------------------------------------------------------------------------

import nuke
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
import PySide2.QtGui as QtGui
from PySide2.QtCore import Qt


from nukescripts import panels

import expression_curves
import utils

class AnimationManagerBeta(QtWidgets.QWidget):
    def __init__(self, parent=None):
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
        self.refreshButton = QtWidgets.QPushButton("Update node")
    #frame range group
        self.group2 = QtWidgets.QGroupBox("New frame range")
        self.myff = QtWidgets.QLineEdit()
        self.myff.setAlignment(QtCore.Qt.AlignLeft)
        self.myff.setFixedWidth(50)
        self.mylf = QtWidgets.QLineEdit()
        self.mylf.setFixedWidth(50)
        self.labelMyff = QtWidgets.QLabel("First frame")
        self.labelMyff.setIndent(1)
        self.labelMylf = QtWidgets.QLabel("Last frame")
    #offset group
        self.offsetGroup = QtWidgets.QGroupBox("Keyframes offset")
        self.offsetLabel = QtWidgets.QLabel("Offset")
        self.offsetValue = QtWidgets.QLineEdit()
        self.offsetValue.setFixedWidth(50)

    #multiply group
        self.multGroup = QtWidgets.QGroupBox("Keyframes multiply")
        self.multLabel = QtWidgets.QLabel("Multiply")
        self.multValue = QtWidgets.QLineEdit()
        self.multValue.setFixedWidth(50)

    #loop group
        self.loopGroup = QtWidgets.QGroupBox("")
        self.loopGroupOffset = QtWidgets.QGroupBox("")
        self.loopGroup2 = QtWidgets.QGroupBox("Loop Animation")
        self.loopButton = QtWidgets.QPushButton("Loop Animation")
        self.loopSlider = QtWidgets.QLineEdit()
        self.loopSlider = QtWidgets.QLineEdit()
        self.loopSlider.setFixedWidth(50)
        self.loopSliderLabel = QtWidgets.QLabel("Offset Animation")
        self.loopSliderLabel.setIndent(1)
        self.loopmyff = QtWidgets.QLineEdit()
        self.loopmyff.setAlignment(QtCore.Qt.AlignLeft)
        self.loopmyff.setFixedWidth(50)
        self.loopmylf = QtWidgets.QLineEdit()
        self.loopmylf.setFixedWidth(50)
        self.looplabelMyff = QtWidgets.QLabel("Offset Loop First frame")
        self.looplabelMyff.setIndent(1)
        self.looplabelMylf = QtWidgets.QLabel("Offset Loop Last frame")
    #creation of layouts
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout1.setAlignment(QtCore.Qt.AlignTop)
        self.in_layout = QtWidgets.QHBoxLayout()
        self.frameRangeLayout = QtWidgets.QHBoxLayout()
        self.frameRangeLayout.addStretch(2)
        self.frameRangeLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.offsetLayout = QtWidgets.QHBoxLayout()
        self.multLayout = QtWidgets.QHBoxLayout()
        self.loopLayout = QtWidgets.QHBoxLayout()
        self.loopOffsetLayout = QtWidgets.QHBoxLayout()
        self.loopOffsetLayout.addStretch(2)
        self.loopOffsetLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.loopframeRangeLayout = QtWidgets.QHBoxLayout()
        self.loopframeRangeLayout.addStretch(2)
        self.loopframeRangeLayout.setAlignment(QtCore.Qt.AlignLeft)
    #adding groups to layouts
        self.layout1.addWidget(self.group1)
        self.layout1.addWidget(self.group2)
        self.layout1.addWidget(self.offsetGroup)
        self.layout1.addWidget(self.multGroup)
        self.layout1.addWidget(self.loopGroup2)
        self.layout1.addWidget(self.loopGroup)
        self.layout1.addWidget(self.loopGroupOffset)

        #adding graphic elements to layouts
        self.in_layout.addWidget(self.label)
        self.in_layout.addWidget(self.combo)
        self.in_layout.addWidget(self.refreshButton)
        self.group1.setLayout(self.in_layout)

        self.loopOffsetLayout.addWidget(self.loopSliderLabel)
        self.loopOffsetLayout.addWidget(self.loopSlider)
        self.loopGroupOffset.setLayout(self.loopOffsetLayout)

        self.loopframeRangeLayout.addWidget(self.looplabelMyff)
        self.loopframeRangeLayout.addWidget(self.loopmyff)
        self.loopframeRangeLayout.addWidget(self.looplabelMylf)
        self.loopframeRangeLayout.addWidget(self.loopmylf)
        self.loopGroup.setLayout(self.loopframeRangeLayout)

        self.frameRangeLayout.addWidget(self.labelMyff)
        self.frameRangeLayout.addWidget(self.myff)
        self.frameRangeLayout.addWidget(self.labelMylf)
        self.frameRangeLayout.addWidget(self.mylf)
        self.group2.setLayout(self.frameRangeLayout)

        self.offsetLayout.addWidget(self.offsetLabel)
        self.offsetLayout.addWidget(self.offsetValue)
        self.offsetGroup.setLayout(self.offsetLayout)

        self.multLayout.addWidget(self.multLabel)
        self.multLayout.addWidget(self.multValue)
        self.multLayout.addWidget(self.loopButton)
        self.multGroup.setLayout(self.multLayout)

        self.loopLayout.addWidget(self.loopButton)

        self.loopGroup2.setLayout(self.loopLayout)

    #adding tab to layout
        self.tab1.setLayout(self.layout1)
        self.tab2 = QtWidgets.QWidget()

#expression curve tab
    #creation of the graphic elements
        self.comboCurve = QtWidgets.QComboBox()
        self.comboCurve.setFixedWidth(150)
        self.labelCurve = QtWidgets.QLabel("Knob")
        self.group1Curve = QtWidgets.QGroupBox("Select knob to animate")

        self.group2Curve = QtWidgets.QGroupBox("Set parameters")
        self.wavelengthLabel = QtWidgets.QLabel("Wavelength")
        self.wavelengthValue = QtWidgets.QLineEdit()
        self.wavelengthValue.setFixedWidth(50)

        self.groupOffsetCurve = QtWidgets.QGroupBox()
        self.offsetLabelCurve = QtWidgets.QLabel("Frame Offset")
        self.offsetValueCurve = QtWidgets.QLineEdit()
        self.offsetValueCurve.setFixedWidth(50)

        self.groupHeight = QtWidgets.QGroupBox()
        self.myffCurve = QtWidgets.QLineEdit()
        self.myffCurve.setFixedWidth(50)
        self.mylfCurve = QtWidgets.QLineEdit()
        self.mylfCurve.setFixedWidth(50)
        self.labelMyffCurve = QtWidgets.QLabel("Minimum value")
        self.labelMyffCurve.setIndent(1)
        self.labelMylfCurve = QtWidgets.QLabel("Maximum value")
    #creation of buttons
        self.groupButtons = QtWidgets.QGroupBox("Generate the curve")
        self.randomButton = QtWidgets.QPushButton("Random")
        self.triangleButton = QtWidgets.QPushButton("Triangle")
        self.sineButton = QtWidgets.QPushButton("Sine")
        self.squareButton = QtWidgets.QPushButton("Square")
        self.sawtoothButton = QtWidgets.QPushButton("Sawtooth")
        self.bounceButton = QtWidgets.QPushButton("Bounce")
    #creation of layouts
        self.in_layoutCurve = QtWidgets.QHBoxLayout()
        self.in_layoutCurve.addWidget(self.labelCurve)
        self.in_layoutCurve.addWidget(self.comboCurve)
        self.group1Curve.setLayout(self.in_layoutCurve)
        self.in_layoutCurve.setAlignment(QtCore.Qt.AlignTop)
    #adding graphic elements to layouts
        self.wavelengthLayout = QtWidgets.QHBoxLayout()
        self.wavelengthLayout.addWidget(self.wavelengthLabel)
        self.wavelengthLayout.addWidget(self.wavelengthValue)

        self.offsetCurveLayout = QtWidgets.QHBoxLayout()
        self.offsetCurveLayout.addWidget(self.offsetLabelCurve)
        self.offsetCurveLayout.addWidget(self.offsetValueCurve)
        #self.offsetCurveLayout.addWidget(self.offsetSliderCurve)

        self.heightCurveLayout = QtWidgets.QHBoxLayout()
        self.heightCurveLayout.addWidget(self.labelMyffCurve)
        self.heightCurveLayout.addWidget(self.myffCurve)
        self.heightCurveLayout.addWidget(self.labelMylfCurve)
        self.heightCurveLayout.addWidget(self.mylfCurve)

        self.buttonsLayout = QtWidgets.QGridLayout()
        self.buttonsLayout.addWidget(self.randomButton, 0,0)
        self.buttonsLayout.addWidget(self.triangleButton, 0,1)
        self.buttonsLayout.addWidget(self.sineButton,0,2)
        self.buttonsLayout.addWidget(self.squareButton,1,0)
        self.buttonsLayout.addWidget(self.sawtoothButton,1,1)
        self.buttonsLayout.addWidget(self.bounceButton,1,2)

        self.group2Curve.setLayout(self.wavelengthLayout)
        self.groupOffsetCurve.setLayout(self.offsetCurveLayout)
        self.groupHeight.setLayout(self.heightCurveLayout)
        self.groupButtons.setLayout(self.buttonsLayout)

#getting the animated knobs of the selected node
        knoblist = utils.getAnimKnobs()
        self.combo.addItems(knoblist)

    #adding groups to layouts
        self.layout2 = QtWidgets.QVBoxLayout()
        self.layout2.addWidget(self.group1Curve)

        self.layout2.addWidget(self.group2Curve)
        self.layout2.addWidget(self.groupOffsetCurve)
        self.layout2.addWidget(self.groupHeight)
        self.layout2.addWidget(self.groupButtons)

        self.layout2.addStretch(2)
        self.tab2.setLayout(self.layout2)

#adding tabs to master layout
        self.tab.addTab(self.tab1, "Adapt custom curve")
        self.tab.addTab(self.tab2, "Curve presets")

        self.titleLabel = QtWidgets.QLabel("Press to update the node")
        self.spaceLabel = QtWidgets.QLabel(" ")
        self.spaceLabel2 = QtWidgets.QLabel(" ")
        self.tabsLabel = QtWidgets.QLabel("Generate or modify your animation curves")
        self.signLabel = QtWidgets.QLabel("by Nacho Igea")

        self.master_layout = QtWidgets.QVBoxLayout()
        self.master_layout.addWidget(self.titleLabel)
        self.master_layout.addWidget(self.spaceLabel)
        self.master_layout.addWidget(self.refreshButton)
        self.master_layout.addWidget(self.spaceLabel2)
        self.master_layout.addWidget(self.tabsLabel)
        self.master_layout.addWidget(self.spaceLabel2)
        self.master_layout.addWidget(self.tab)
        self.master_layout.addWidget(self.spaceLabel2)
        self.master_layout.addWidget(self.signLabel)

#getting all the knobs in the selected node
        allknoblist = utils.getAllKnobs()
        self.comboCurve.addItems(allknoblist)
#setting values for the inputs

        isAnim = utils.checkAnimation()
        if isAnim == True:

            firstFrame = utils.getFirstFrame(self.combo)
            self.myff.setText(str(firstFrame))

            lastFrame = utils.getLastFrame(self.combo)
            self.mylf.setText(str(lastFrame))

        self.offsetValue.setText(str(0))
        self.multValue.setText(str(1))

        self.loopmyff.setText(str(0))
        self.loopmylf.setText(str(0))
        self.loopSlider.setText(str(0))

        self.wavelengthValue.setText(str(10))
        self.offsetValueCurve.setText(str(0))
        self.myffCurve.setText(str(0))
        self.mylfCurve.setText(str(1))

#adding functions to text boxes in custom curves tab
        self.offsetValue.returnPressed.connect(lambda : self.addOffsetEdit(self.combo, self.offsetValue))
        self.multValue.returnPressed.connect(lambda : self.multiplyEdit(self.combo, self.multValue))
        self.myff.returnPressed.connect(lambda : self.adaptAnimFF(self.myff, self.combo))
        self.mylf.returnPressed.connect(lambda : self.adaptAnimLF(self.mylf, self.combo))

        self.loopSlider.returnPressed.connect(lambda : self.offsetAnim(self.combo, self.loopSlider, self.loopmylf, self.loopmyff))
        self.loopmyff.returnPressed.connect(lambda : self.offsetAnim(self.combo, self.loopSlider, self.loopmylf, self.loopmyff))
        self.loopmylf.returnPressed.connect(lambda : self.offsetAnim(self.combo, self.loopSlider, self.loopmylf, self.loopmyff))

#adding functions to push buttons in expression curve tab
        preset_curves= expression_curves.Curves(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.mylfCurve, self.myffCurve)
        self.randomButton.clicked.connect(lambda : preset_curves.random_curve())
        self.triangleButton.clicked.connect(lambda : preset_curves.triangle_curve())
        self.sineButton.clicked.connect(lambda : preset_curves.sin_curve())
        self.squareButton.clicked.connect(lambda : preset_curves.square_curve())
        self.sawtoothButton.clicked.connect(lambda : preset_curves.sawtooth_curve())
        self.bounceButton.clicked.connect(lambda: preset_curves.bounce_curve())


#addinf functions to buttons and pulldown in custom curve tab
        self.loopButton.clicked.connect(lambda : self.loopAnim(self.combo))
        self.refreshButton.clicked.connect(lambda : self.refreshFunction())
        self.combo.currentTextChanged.connect(lambda : self.refreshKnob(self.combo))

        self.setLayout(self.master_layout)
        self.setGeometry(30, 30, 30, 15)

        self.refreshKnob(self.combo)

#this functions updates the panel when a different node is selected from the original
    def refreshFunction(self):
        # reuse existing logic to get knobs of current selected node.
        self.combo.clear()
        self.combo.addItems(utils.getAnimKnobs())

        isAnim = utils.checkAnimation()

        self.myff.clear()
        self.mylf.clear()

        if isAnim == True:

            firstFrame = utils.getFirstFrame(self.combo)
            self.myff.setText(str(firstFrame))

            lastFrame = utils.getLastFrame(self.combo)
            self.mylf.setText(str(lastFrame))

        self.comboCurve.clear()
        self.comboCurve.addItems(utils.getAllKnobs())

#this function hides the parameters in the custom curve tab if the knob selected in the pulldown has an expression and shows them if it doesn't
    def refreshKnob(self, k):

        isAnim = utils.checkAnimation()

        self.myff.clear()
        self.mylf.clear()

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        isString = utils.findStringCurve(actKnob, 'curve')

        if isAnim == True:
            if actKnob.hasExpression() == False:

                firstFrame = utils.getFirstFrame(self.combo)
                self.myff.setText(str(firstFrame))

                lastFrame = utils.getLastFrame(self.combo)
                self.mylf.setText(str(lastFrame))

            elif actKnob.hasExpression() == True and isString == 1:

                firstFrame = utils.getFirstFrame(self.combo)
                self.myff.setText(str(firstFrame))

                lastFrame = utils.getLastFrame(self.combo)
                self.mylf.setText(str(lastFrame))

        if actKnob.hasExpression() == True and isString == 0:

            self.group2.hide()
            self.offsetGroup.hide()
            self.multGroup.hide()
            self.loopGroup.hide()
            self.loopGroupOffset.hide()
            self.loopGroup2.hide()
        elif actKnob.hasExpression() == True and isString == 1:

            self.group2.show()
            self.offsetGroup.show()
            self.multGroup.show()
            self.loopGroup.show()
            self.loopGroupOffset.show()
            self.loopGroup2.show()
        elif actKnob.hasExpression() == False:

            self.group2.show()
            self.offsetGroup.show()
            self.multGroup.show()
            self.loopGroup.show()
            self.loopGroupOffset.show()
            self.loopGroup2.show()

#this function adds the introduced offset to the whole custom curve
    def addOffsetEdit(self,k, offsetSliderFun):

            keyList = utils.getAnimKeyFrame(k)
            if offsetSliderFun.text():
                addedOffset = offsetSliderFun.text()
            else:
                addedOffset = str(0)

            min_prev_frame = keyList[0]
            max_prev_frame = keyList[-1]

            selKnob = k.currentText()
            actKnob = nuke.selectedNode().knob(selKnob)

            animCurve = actKnob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

            x_pos = []
            y_pos = []
            for key in animCurve.keys():

                xValue = int(key.x)
                yValue = float(key.y)
                x_pos.append(xValue)
                y_pos.append(yValue)
                animCurve.clear()

            offset = []
            actKnob.setAnimated()

            for c in range(len(x_pos)):

                suma = (y_pos[c] + float(addedOffset))
                offset.append(suma)
                actKnob.setValueAt(offset[c], x_pos[c])
                c = c + 1

            return offset

#this function multiplies all y values of the keyframes with the inctroduced factor
    def multiplyEdit(self,k, multiplyFun):

            keyList = utils.getAnimKeyFrame(k)

            if multiplyFun.text():
                addedMult = multiplyFun.text()
            else:
                addedMult = str(0)

            min_prev_frame = keyList[0]
            max_prev_frame = keyList[-1]

            selKnob = k.currentText()
            actKnob = nuke.selectedNode().knob(selKnob)

            animCurve = actKnob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

            x_pos = []
            y_pos = []
            for key in animCurve.keys():

                xValue = int(key.x)
                yValue = float(key.y)
                x_pos.append(xValue)
                y_pos.append(yValue)
                animCurve.clear()

            multList = []
            actKnob.setAnimated()

            for c in range(len(x_pos)):

                mult = (y_pos[c] * float(addedMult))
                multList.append(mult)
                actKnob.setValueAt(multList[c], x_pos[c])
                c = c + 1

            return multList

#this function changes the first keyframe while adapting the rest of the keyframes of the curve
    def adaptAnimFF(self, myff,k):

        keyList = utils.getAnimKeyFrame(k)

        min_set_frame = myff.text()
        #max_set_frame = mylf.text()

        min_prev_frame = keyList[0]
        max_prev_frame = keyList[-1]

        original_range = max_prev_frame - min_prev_frame
        new_range = max_prev_frame - int(min_set_frame)
        kmult = new_range / float(original_range)

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        animCurve = actKnob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

        x_pos = []
        y_pos = []
        for key in animCurve.keys():

            xValue = int(key.x)
            yValue = float(key.y)
            x_pos.append(xValue)
            y_pos.append(yValue)
            animCurve.clear()

        offset = []
        actKnob.setAnimated()

        for c in range(len(x_pos)):
            suma = (x_pos[c] - min_prev_frame)*(kmult)
            final_key = int(min_set_frame) + int(suma)
            entero = int(final_key)
            offset.append(entero)
            actKnob.setValueAt(y_pos[c], offset[c])
            c = c + 1

        return entero

#this function changes the last keyframe while adapting the rest of the keyframes of the curve
    def adaptAnimLF(self, mylf,k):

        keyList = utils.getAnimKeyFrame(k)

        #min_set_frame = myff.text()
        max_set_frame = mylf.text()

        min_prev_frame = keyList[0]
        max_prev_frame = keyList[-1]

        original_range = max_prev_frame - min_prev_frame
        new_range = int(max_set_frame) - min_prev_frame
        kmult = new_range / float(original_range)

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        animCurve = actKnob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

        x_pos = []
        y_pos = []
        for key in animCurve.keys():

            xValue = int(key.x)
            yValue = float(key.y)
            x_pos.append(xValue)
            y_pos.append(yValue)
            animCurve.clear()

        offset = []
        actKnob.setAnimated()

        for c in range(len(x_pos)):
            suma = (x_pos[c] - min_prev_frame)*(kmult)
            final_key = int(min_prev_frame) + int(suma)
            entero = int(final_key)
            offset.append(entero)
            actKnob.setValueAt(y_pos[c], offset[c])
            c = c + 1

        return entero

    def offsetAnim(self, k, loopOffset, lastframeoffset, firstframeoffset):

        loopFirstFrame = utils.getFirstFrame(k)
        loopLastFrame = utils.getLastFrame(k)

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        strLff = str(loopFirstFrame)
        strLlf = str(loopLastFrame)

        if loopOffset.text() == '':

            frameOffset = str(0)
        else:
            frameOffset = loopOffset.text()
        if lastframeoffset.text() == '':
            paramlastframeoffset = str(0)

        else:
            paramlastframeoffset = lastframeoffset.text()
        if firstframeoffset.text() == '':

            paramfirstframeoffset = str(0)
        else:
            paramfirstframeoffset = firstframeoffset.text()

        actKnob.setExpression("curve(((frame-" + strLff +"+" + frameOffset + ")%(" + strLlf +"-" + strLff + "-" + paramfirstframeoffset + "+" + paramlastframeoffset + "+1))+" + strLff +" )")

    def loopAnim(self, k):

        loopFirstFrame = utils.getFirstFrame(k)
        loopLastFrame = utils.getLastFrame(k)

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        strLff = str(loopFirstFrame)
        strLlf = str(loopLastFrame)

        actKnob.setExpression("curve(((frame-" + strLff +")%(" + strLlf +"-" + strLff +"+1))+" + strLff +" )")

nuke.menu( 'Nuke' ).addCommand('Animation Manager', lambda: AnimationManagerBeta().show())