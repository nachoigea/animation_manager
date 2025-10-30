import nuke

import utils

def loop_anim(k):
    """Add expression to selected knob to loop the existing animation

    :param k: knob to perform the action

    """
    loop_first_frame = utils.get_first_frame(k)
    loop_last_frame = utils.get_last_frame(k)

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    act_knob.setExpression(f"curve(((frame- {str(loop_first_frame)} )%( {str(loop_last_frame)} - "
                          f"{str(loop_first_frame)} +1))+ {str(loop_first_frame)} )"
                          )

def offset_anim(k, loop_offset, last_frame_offset, first_frame_offset):
    """Move the existing animation in time (x-axis) by the specified offset

    :param k: knob to perform the action
    :param loop_offset: amount of frames to offset the animation
    :param last_frame_offset: last frame to offset the animation
    :param first_frame_offset: first frame to offset the animation
    """

    loop_first_frame = utils.get_first_frame(k)
    loop_last_frame = utils.get_last_frame(k)

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    if loop_offset.text() == '':

        frame_offset = str(0)
    else:
        frame_offset = loop_offset.text()
    if last_frame_offset.text() == '':
        param_last_frame_offset = str(0)

    else:
        param_last_frame_offset = last_frame_offset.text()
    if first_frame_offset.text() == '':

        param_first_frame_offset = str(0)
    else:
        param_first_frame_offset = first_frame_offset.text()

    act_knob.setExpression(f"curve(((frame- {str(loop_first_frame)} + {frame_offset} )%( {str(loop_last_frame)} "
                          f"- {str(loop_first_frame)} - {param_first_frame_offset} + {param_last_frame_offset} "
                          f"+1))+ {str(loop_first_frame)} )"
                          )

def adapt_anim_last_frame(my_last_frame,k):
    """Adapt the aimation to change the last frame, rest of the frames are computed accordingly

    :param my_last_frame: new last frame to adapt the animation to
    :param k: knob to perform the action
    :return:
    """

    key_list = utils.get_anim_keyframe(k)

    max_set_frame = my_last_frame.text()

    min_prev_frame = key_list[0]
    max_prev_frame = key_list[-1]

    original_range = max_prev_frame - min_prev_frame
    new_range = int(max_set_frame) - min_prev_frame
    k_mult = new_range / float(original_range)

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    anim_curve = act_knob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

    x_pos = []
    y_pos = []
    for key in anim_curve.keys():

        x_value = int(key.x)
        y_value = float(key.y)
        x_pos.append(x_value)
        y_pos.append(y_value)
        anim_curve.clear()

    offset = []
    act_knob.setAnimated()

    for c in range(len(x_pos)):
        suma = (x_pos[c] - min_prev_frame)*k_mult
        final_key = int(min_prev_frame) + int(suma)
        int_final_key = int(final_key)
        offset.append(int_final_key)
        act_knob.setValueAt(y_pos[c], offset[c])
        c = c + 1

    return int_final_key

def adapt_anim_first_frame(my_first_frame,k):
    """Adapt the aimation to change the first frame, rest of the frames are computed accordingly

    :param my_first_frame: new first frame to adapt the animation to
    :param k: knob to perform the action
    :return:
    """

    key_list = utils.get_anim_keyframe(k)

    min_set_frame = my_first_frame.text()

    min_prev_frame = key_list[0]
    max_prev_frame = key_list[-1]

    original_range = max_prev_frame - min_prev_frame
    new_range = max_prev_frame - int(min_set_frame)
    k_mult = new_range / float(original_range)

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    anim_curve = act_knob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

    x_pos = []
    y_pos = []
    for key in anim_curve.keys():

        x_value = int(key.x)
        y_value = float(key.y)
        x_pos.append(x_value)
        y_pos.append(y_value)
        anim_curve.clear()

    offset = []
    act_knob.setAnimated()

    for c in range(len(x_pos)):
        suma = (x_pos[c] - min_prev_frame)*k_mult
        final_key = int(min_set_frame) + int(suma)
        int_final_key = int(final_key)
        offset.append(int_final_key)
        act_knob.setValueAt(y_pos[c], offset[c])
        c = c + 1

    return int_final_key

def multiply_edit(k, multiply_fun):
    """Multiply all y values of the keyframes with the introduced factor

    :param k: knob to perform the action
    :param multiply_fun: factor to multiply the y values
    :return: list of the y-values multiplied by the introduced factor
    """

    if multiply_fun.text():
        added_mult = multiply_fun.text()
    else:
        added_mult = str(0)


    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    anim_curve = act_knob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

    x_pos = []
    y_pos = []
    for key in anim_curve.keys():

        x_value = int(key.x)
        y_value = float(key.y)
        x_pos.append(x_value)
        y_pos.append(y_value)
        anim_curve.clear()

    mult_list = []
    act_knob.setAnimated()

    for c in range(len(x_pos)):

        mult = (y_pos[c] * float(added_mult))
        mult_list.append(mult)
        act_knob.setValueAt(mult_list[c], x_pos[c])
        c = c + 1

    return mult_list

def add_offset_edit(k, offset_slider_fun):
    """Add the introduced offset to the whole custom curve

    :param k: knob to perform the action
    :param offset_slider_fun: offset amount to move the animation
    :return:
    """

    if offset_slider_fun.text():
        added_offset = offset_slider_fun.text()
    else:
        added_offset = str(0)

    sel_knob = k.currentText()
    act_knob = nuke.selectedNode().knob(sel_knob)

    anim_curve = act_knob.animation( 0 ) #ANIMATION IN THE FIRST FIELD (X VALUE)

    x_pos = []
    y_pos = []
    for key in anim_curve.keys():

        x_value = int(key.x)
        y_value = float(key.y)
        x_pos.append(x_value)
        y_pos.append(y_value)
        anim_curve.clear()

    offset = []
    act_knob.setAnimated()

    for c in range(len(x_pos)):

        suma = (y_pos[c] + float(added_offset))
        offset.append(suma)
        act_knob.setValueAt(offset[c], x_pos[c])
        c = c + 1

    return offset