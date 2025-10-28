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
        knoblist = self.getAnimKnobs()
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
        allknoblist = self.getAllKnobs()
        self.comboCurve.addItems(allknoblist)
#setting values for the inputs

        isAnim = self.checkAnimation()
        if isAnim == True:

            firstFrame = self.getFirstFrame(self.combo)
            self.myff.setText(str(firstFrame))

            lastFrame = self.getLastFrame(self.combo)
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
        self.randomButton.clicked.connect(lambda : self.randomCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.myffCurve, self.mylfCurve ))
        self.triangleButton.clicked.connect(lambda : self.triangleCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.myffCurve, self.mylfCurve ))
        self.sineButton.clicked.connect(lambda : self.sinCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.myffCurve, self.mylfCurve ))
        self.squareButton.clicked.connect(lambda : self.squareCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.myffCurve, self.mylfCurve ))
        self.sawtoothButton.clicked.connect(lambda : self.sawtoothCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.mylfCurve, self.myffCurve ))
        #self.bounceButton.clicked.connect(lambda : self.bounceCurve(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.mylfCurve, self.myffCurve ))

        inherited_curves= expression_curves.Curves(self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.mylfCurve, self.myffCurve)
        self.bounceButton.clicked.connect(lambda: inherited_curves.compute_bounce_curve(
            self.comboCurve, self.wavelengthValue, self.offsetValueCurve, self.mylfCurve, self.myffCurve
            ))

#addinf functions to buttons and pulldown in custom curve tab
        self.loopButton.clicked.connect(lambda : self.loopAnim(self.combo))
        self.refreshButton.clicked.connect(lambda : self.refreshFunction())
        self.combo.currentTextChanged.connect(lambda : self.refreshKnob(self.combo))

        self.setLayout(self.master_layout)
        self.setGeometry(30, 30, 30, 15)

        self.refreshKnob(self.combo)


#this functions sets an integer to 1 if the substring is found in the sring
    def findStringCurve(self, currentKnob, searchString):

        stringFound = 0
        origExpression = ''
        index = 0
        if currentKnob.hasExpression():
            origExpression = currentKnob.animation(index).expression()

        if (origExpression.find(searchString) != -1):
            stringFound = 1
        else:
            stringFound = 0

        return stringFound

#this function checks if there is a knob animated in the selected node
    def checkAnimation(self):

        mynode = nuke.selectedNode()

        knobList = []
        animKnobList = []
        count = 0
        for i in mynode.knobs():
            knobList.append(i)
            if mynode.knob(knobList[count]).isAnimated():
                animKnobList.append(i)
            count = count + 1

        isAnimFun = bool(animKnobList)
        return isAnimFun

#this function gets all the animated knobs in the selected node
    def getAnimKnobs(self):

        mynode = nuke.selectedNode()

        knobList = []
        animKnobList = []
        count = 0
        for i in mynode.knobs():
            knobList.append(i)
            if mynode.knob(knobList[count]).isAnimated():
                animKnobList.append(i)
            count = count + 1

        return animKnobList

#this functions updates the panel when a different node is selected from the original
    def refreshFunction(self):
        # reuse existing logic to get knobs of current selected node.
        self.combo.clear()
        self.combo.addItems(self.getAnimKnobs())

        isAnim = self.checkAnimation()

        self.myff.clear()
        self.mylf.clear()

        if isAnim == True:

            firstFrame = self.getFirstFrame(self.combo)
            self.myff.setText(str(firstFrame))

            lastFrame = self.getLastFrame(self.combo)
            self.mylf.setText(str(lastFrame))

        self.comboCurve.clear()
        self.comboCurve.addItems(self.getAllKnobs())

#this function hides the parameters in the custom curve tab if the knob selected in the pulldown has an expression and shows them if it doesn't
    def refreshKnob(self, k):

        isAnim = self.checkAnimation()

        self.myff.clear()
        self.mylf.clear()

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        isString = self.findStringCurve(actKnob, 'curve')

        if isAnim == True:
            if actKnob.hasExpression() == False:

                firstFrame = self.getFirstFrame(self.combo)
                self.myff.setText(str(firstFrame))

                lastFrame = self.getLastFrame(self.combo)
                self.mylf.setText(str(lastFrame))

            elif actKnob.hasExpression() == True and isString == 1:

                firstFrame = self.getFirstFrame(self.combo)
                self.myff.setText(str(firstFrame))

                lastFrame = self.getLastFrame(self.combo)
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

#this function gets the first frame of the animation in the selected knob
    def getFirstFrame(self, k):

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        xValueList = []
        #if actKnob.hasExpression() == False:
        #print "This knob has an expression in getFirstFrame"
        animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)

        isString = self.findStringCurve(actKnob, 'curve')

        if actKnob.hasExpression() == False:
            for key in animCurve.keys():
                xValue = key.x
                xValueList.append(xValue)

            return xValueList[0]

        if actKnob.hasExpression() == True  and isString == 1:
            for key in animCurve.keys():
                xValue = key.x
                xValueList.append(xValue)

            return xValueList[0]

#this function gets the last frame of the animation in the selected knob
    def getLastFrame(self, k):

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        #if actKnob.hasExpression() == False:
        animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
        xValueList = []

        isString = self.findStringCurve(actKnob, 'curve')

        if actKnob.hasExpression() == False:
            for key in animCurve.keys():
                xValue = key.x
                xValueList.append(xValue)

            return xValueList[-1]

        if actKnob.hasExpression() == True   and isString == 1:
            for key in animCurve.keys():
                xValue = key.x
                xValueList.append(xValue)

            return xValueList[-1]

#this function gets all the knobs in the selected node
    def getAllKnobs(self):

        mynode = nuke.selectedNode()

        knobList = []
        animKnobList = []
        delList = ['Mask','label', 'note_font','note_font_size','note_font_color','hide_input','cached','disable','dope_sheet','bookmark','postage_stamp','postage_stamp_frame','lifetimeStart','lifetimeEnd','useLifetime','tile_color','gl_color','name','help','knobChanged','onDestroy','updateUI','rootNodeUpdated','dope_sheet','icon','panel','indicators','onCreate','autolabel']
        count = 0

        for i in mynode.knobs():
            knobList.append(i)
            count = count + 1

        knobList.sort()

        for i in range(len(delList)):
            if delList[i] in knobList:

                knobList.pop(knobList.index(delList[i]))

        return knobList

#this function gets all the keyframes of the selected animated knob
    def getAnimKeyFrame(self, k):

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)
        animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
        xValueList = []

        for key in animCurve.keys():
            xValue = key.x
            xValueList.append(xValue)

        return xValueList

#this function adds the introduced offset to the whole custom curve
    def addOffsetEdit(self,k, offsetSliderFun):

            keyList = self.getAnimKeyFrame(k)
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

            keyList = self.getAnimKeyFrame(k)

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

        keyList = self.getAnimKeyFrame(k)

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

        keyList = self.getAnimKeyFrame(k)

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

        loopFirstFrame = self.getFirstFrame(k)
        loopLastFrame = self.getLastFrame(k)

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

        loopFirstFrame = self.getFirstFrame(k)
        loopLastFrame = self.getLastFrame(k)

        selKnob = k.currentText()
        actKnob = nuke.selectedNode().knob(selKnob)

        strLff = str(loopFirstFrame)
        strLlf = str(loopLastFrame)

        actKnob.setExpression("curve(((frame-" + strLff +")%(" + strLlf +"-" + strLff +"+1))+" + strLff +" )")


#this function creates the sine function when the button is pressed
    def sinCurve(self, k, WLstr, Offsetstr, maxstr, minstr):

        selKnob = k.currentText()

        actKnob = nuke.selectedNode().knob(selKnob)

        if WLstr.text() == '':

            paramWL = str(1)
        else:
            paramWL = WLstr.text()
        if Offsetstr.text() == '':
            paramOffset = str(0)

        else:
            paramOffset = Offsetstr.text()
        if maxstr.text() == '':

            paramMax = str(1)
        else:
            paramMax = maxstr.text()
        if minstr.text() == '':

            paramMin = str(0)
        else:
            paramMin = minstr.text()

        actKnob.setExpression("(sin(2*pi*(frame+" + paramOffset + ")/" + paramWL + ")+1)/2 *(" + paramMax + "-" + paramMin + ") + " + paramMin )


#this function creates the square function when the button is pressed
    def squareCurve(self, k, WLstr, Offsetstr, maxstr, minstr):

        selKnob = k.currentText()

        actKnob = nuke.selectedNode().knob(selKnob)

        if WLstr.text() == '':

            paramWL = str(1)
        else:
            paramWL = WLstr.text()
        if Offsetstr.text() == '':
            paramOffset = str(0)

        else:
            paramOffset = Offsetstr.text()
        if maxstr.text() == '':

            paramMax = str(1)
        else:
            paramMax = maxstr.text()
        if minstr.text() == '':

            paramMin = str(0)
        else:
            paramMin = minstr.text()

        actKnob.setExpression("int(sin(2*pi*(frame+" + paramOffset + ")/" + paramWL + ")+1)/2 *(" + paramMax + "-" + paramMin + ")*2 + " + paramMin )



#this function creates the random function when the button is pressed
    def randomCurve(self, k, WLstr, Offsetstr, maxstr, minstr):

        selKnob = k.currentText()

        actKnob = nuke.selectedNode().knob(selKnob)

        if WLstr.text() == '':

            paramWL = str(1)
        else:
            paramWL = WLstr.text()
        if Offsetstr.text() == '':
            paramOffset = str(0)

        else:
            paramOffset = Offsetstr.text()
        if maxstr.text() == '':

            paramMax = str(1)
        else:
            paramMax = maxstr.text()
        if minstr.text() == '':

            paramMin = str(0)
        else:
            paramMin = minstr.text()

        actKnob.setExpression("((random(frame+" + paramOffset + "))) *(" + paramMax + "-" + paramMin + ") + " + paramMin )


#this function creates the triangle function when the button is pressed
    def triangleCurve(self, k, WLstr, Offsetstr, maxstr, minstr):

        selKnob = k.currentText()

        actKnob = nuke.selectedNode().knob(selKnob)

        if WLstr.text() == '':

            paramWL = str(1)
        else:
            paramWL = WLstr.text()
        if Offsetstr.text() == '':
            paramOffset = str(0)

        else:
            paramOffset = Offsetstr.text()
        if maxstr.text() == '':

            paramMax = str(1)
        else:
            paramMax = maxstr.text()
        if minstr.text() == '':

            paramMin = str(0)
        else:
            paramMin = minstr.text()

        actKnob.setExpression("(asin(sin(2*pi*(frame+" + paramOffset + ")/" + paramWL + "))/pi+0.5) *(" + paramMax + "-" + paramMin + ") + " + paramMin )

#this function creates the swatooth function when the button is pressed
    def sawtoothCurve(self, k, WLstr, Offsetstr, maxstr, minstr):

        selKnob = k.currentText()

        actKnob = nuke.selectedNode().knob(selKnob)

        if WLstr.text() == '':

            paramWL = str(1)
        else:
            paramWL = WLstr.text()
        if Offsetstr.text() == '':
            paramOffset = str(0)

        else:
            paramOffset = Offsetstr.text()
        if maxstr.text() == '':

            paramMax = str(1)
        else:
            paramMax = maxstr.text()
        if minstr.text() == '':

            paramMin = str(0)
        else:
            paramMin = minstr.text()

        actKnob.setExpression("((frame+" + paramOffset + ")%" + paramWL + ")/" + paramWL + "*(" + paramMax + "- " + paramMin + ")+" + paramMin )


panels.registerWidgetAsPanel('AnimationManagerBeta', 'AnimationManager', 'uk.co.thefoundry.NukeTestWindow')
print("checking")
#panels.registerWidgetAsPanel('AnimationManager', 'Animation Manager', 'panel.id')
nuke.menu( 'Nuke' ).addCommand('Animation Manager', lambda: AnimationManagerBeta().show())