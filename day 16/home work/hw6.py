def get_size(w,h,d):
    surface_area = 2 * (w * d + w * h + d * h)
    volume = w * h * d
    return [surface_area, volume]