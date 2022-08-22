from urllib import request
from docx import Document


def create_doc(form):
    if form.is_valid(form):
        address = form.cleaned_data.get("address")  # Адрес
        floor = form.cleaned_data.get("floor")  # Этажность
        walls = form.cleaned_data.get("walls")  # Материал стен
        vestibule = form.cleaned_data.get("vestibule")  # тамбура (True-false)
        number_of_vestibules = form.cleaned_data.get("number_of_vestibules")  # Количество тамбуров
        ceiling = form.cleaned_data.get("ceiling")  # Потолок подъезда
        ceiling_vestibule = form.cleaned_data.get("ceiling_vestibule")  # Потолок тамбуров
        painted_walls = form.cleaned_data.get("painted_walls")  # Подъезд окраска стен
        painted_walls_vestibule = form.cleaned_data.get("painted_walls_vestibule")  # Подъезд окраска тамбуров
        whitewash_walls = form.cleaned_data.get("whitewash_walls")  # Окраска по побелке стен подъезда
        whitewash_walls_vestibule = form.cleaned_data.get(
            "whitewash_walls_vestibule")  # Окраска по побелке стен тамбуров
        number_windows = form.cleaned_data.get("number_windows")  # Количество окон
        windows_size = form.cleaned_data.get("windows_size")  # Объём окна
        railing = form.cleaned_data.get("railing")  # Площадь перил
        butt_stairs = form.cleaned_data.get("butt_stairs")  # Площадь торца лестницы
        pipe_coloring = form.cleaned_data.get("pipe_coloring")  # Площадь окраски труб

    # Всего окраски потолка тамбуров
    def all_ceiling_vestibules():
        if number_of_vestibules != 0:
            final_ceiling_vestibule = number_of_vestibules * ceiling_vestibule
        else:
            final_ceiling_vestibule = None

        return final_ceiling_vestibule

    # Всего окраски стен тамбуров
    def all_painted_walls_vestibules():
        if number_of_vestibules != 0:
            final_painted_walls_vestibule = number_of_vestibules * painted_walls_vestibule
        else:
            final_painted_walls_vestibule = None

        return final_painted_walls_vestibule

    # Всего окраски по побелки
    def all_whitewash_walls_vestibules():
        if number_of_vestibules != 0:
            final_whitewash_walls_vestibule = number_of_vestibules * whitewash_walls_vestibule
        else:
            final_whitewash_walls_vestibule = None
        return final_whitewash_walls_vestibule

    # Всего потолка
    def final_entrance(final_ceiling_vestibule):
        final_ceiling = ceiling + final_ceiling_vestibule
        return final_ceiling

    # Всего окраски стен по краске
    def all_painted_walls(final_painted_walls_vestibule):
        final_painted_walls = final_painted_walls_vestibule + painted_walls
        return final_painted_walls

    # Всего окраски по побелке
    def all_whitewash_walls(final_whitewash_walls_vestibule):
        final_whitewash_walls = final_whitewash_walls_vestibule + whitewash_walls
        return final_whitewash_walls

    # Шпатлевание
    def all_puttying(final_painted_walls, final_whitewash_walls):
        puttying = final_painted_walls + final_whitewash_walls
        return puttying

    # Всего расчистки
    def all_clearing(final_painted_walls, final_whitewash_walls):
        clearing = final_painted_walls + final_whitewash_walls
        return clearing

    # Окраска окон
    def windows():
        if number_windows != 0:
            final_paint_windows = number_windows * windows_size
        else:
            final_paint_windows = '0'
        return final_paint_windows

    # Штукатурка стен
    def all_wall_plaster(final_painted_walls, final_whitewash_walls):
        if walls == 'brick':
            wall_plaster = ((final_painted_walls + final_whitewash_walls) / 100) * 35
        else:
            wall_plaster = None
        return wall_plaster

    # Ремонт рустов
    def all_seam():
        if walls == 'Panel':
            seam = floor * 7
        else:
            seam = None
        return seam

    def create_exel():

        doc = Document(r'C:\Users\mavri\PycharmProjects\Django_parser_lerning\mysite\my_job\documents')
        p = doc.add_paragraph(address)

        return doc
    return create_exel()

