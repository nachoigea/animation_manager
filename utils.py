import nuke

#this functions sets an integer to 1 if the substring is found in the sring
def find_string_curve(current_knob, search_string):

    original_expression = ''
    index = 0
    if current_knob.hasExpression():
        original_expression = current_knob.animation(index).expression()

    if original_expression.find(search_string) != -1:
        string_found = 1
    else:
        string_found = 0

    return string_found


#this function gets the first frame of the animation in the selected knob
def get_first_frame(k):

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    x_value_list = []
    anim_curve = act_knob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)

    is_string = find_string_curve(act_knob, 'curve')

    if not act_knob.hasExpression():
        for key in anim_curve.keys():
            x_value = key.x
            x_value_list.append(x_value)

        return x_value_list[0]

    if act_knob.hasExpression() == True and is_string == 1:
        for key in anim_curve.keys():
            x_value = key.x
            x_value_list.append(x_value)

        return x_value_list[0]
    return None


#this function gets the last frame of the animation in the selected knob
def get_last_frame(k):

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    anim_curve = act_knob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
    x_value_list = []

    is_string = find_string_curve(act_knob, 'curve')

    if not act_knob.hasExpression():
        for key in anim_curve.keys():
            x_value = key.x
            x_value_list.append(x_value)

        return x_value_list[-1]

    if act_knob.hasExpression() == True and is_string == 1:
        for key in anim_curve.keys():
            x_value = key.x
            x_value_list.append(x_value)

        return x_value_list[-1]
    return None


#this function gets all the knobs in the selected node
def get_all_knobs():

    mynode = nuke.selectedNode()

    knob_list = []
    del_list = ['Mask','label', 'note_font','note_font_size','note_font_color','hide_input','cached','disable','dope_sheet','bookmark','postage_stamp','postage_stamp_frame','lifetimeStart','lifetimeEnd','useLifetime','tile_color','gl_color','name','help','knobChanged','onDestroy','updateUI','rootNodeUpdated','dope_sheet','icon','panel','indicators','onCreate','autolabel']
    count = 0

    for i in mynode.knobs():
        knob_list.append(i)
        count = count + 1

    knob_list.sort()

    for i in range(len(del_list)):
        if del_list[i] in knob_list:

            knob_list.pop(knob_list.index(del_list[i]))

    return knob_list

#this function gets all the keyframes of the selected animated knob
def get_anim_keyframe(k):

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)
    anim_curve = act_knob.animation(0) #ANIMATION IN THE FIRST FIELD (X VALUE)
    x_value_list = []

    for key in anim_curve.keys():
        x_value = key.x
        x_value_list.append(x_value)

    return x_value_list

#this function gets all the animated knobs in the selected node
def get_anim_knobs():

    mynode = nuke.selectedNode()

    knob_list = []
    anim_knob_list = []
    count = 0
    for i in mynode.knobs():
        knob_list.append(i)
        if mynode.knob(knob_list[count]).isAnimated():
            anim_knob_list.append(i)
        count = count + 1

    return anim_knob_list

#this function checks if there is a knob animated in the selected node
def check_animation():

    mynode = nuke.selectedNode()

    knob_list = []
    anim_knob_list = []
    count = 0
    for i in mynode.knobs():
        knob_list.append(i)
        if mynode.knob(knob_list[count]).isAnimated():
            anim_knob_list.append(i)
        count = count + 1

    is_anim_fun = bool(anim_knob_list)
    return is_anim_fun