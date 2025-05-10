
def scale_widget(widget_width, widget_original_width, widget_original_height):
    
    factor = widget_original_height/widget_original_width
    
    widget_new_width = widget_width
    height_new_height = widget_width*factor
    
    return (widget_new_width, height_new_height)

def scale_widget_relative_to_window(window_width, window_height, widget_relative_width, widget_original_width, widget_original_height):
    
    (widget_new_width, height_new_height) = scale_widget(window_width*widget_relative_width, widget_original_width, widget_original_height)

    return (widget_new_width/window_width, height_new_height/window_height)
    
def get_widget_height():
    h = 0
    return h