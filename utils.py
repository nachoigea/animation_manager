import nuke

#this functions sets an integer to 1 if the substring is found in the sring
def findStringCurve(currentKnob, searchString):

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


#this function gets the first frame of the animation in the selected knob
def getFirstFrame(k):

    selKnob = k.currentText()
    actKnob = nuke.selectedNode().knob(selKnob)

    xValueList = []
    #if actKnob.hasExpression() == False:
    #print "This knob has an expression in getFirstFrame"
    animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)

    isString = findStringCurve(actKnob, 'curve')

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
def getLastFrame(k):

    selKnob = k.currentText()
    actKnob = nuke.selectedNode().knob(selKnob)

    #if actKnob.hasExpression() == False:
    animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
    xValueList = []

    isString = findStringCurve(actKnob, 'curve')

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
def getAllKnobs():

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
def getAnimKeyFrame(k):

    selKnob = k.currentText()
    actKnob = nuke.selectedNode().knob(selKnob)
    animCurve = actKnob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
    xValueList = []

    for key in animCurve.keys():
        xValue = key.x
        xValueList.append(xValue)

    return xValueList

#this function gets all the animated knobs in the selected node
def getAnimKnobs():

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

#this function checks if there is a knob animated in the selected node
def checkAnimation():

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